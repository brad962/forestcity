#!/usr/bin/env python3
"""Forest City AI Office — local dashboard server. Run this, then open the dashboard in your browser."""
import http.server
import json
import os
import re
import socketserver
import sys
import urllib.request
import urllib.error
from urllib.parse import urlparse, parse_qs, urlencode
from pathlib import Path

# Make integrations importable
sys.path.insert(0, str(Path(__file__).parent))

BASE_DIR      = Path(__file__).parent.resolve()
LOG_FILE      = BASE_DIR / 'logs' / 'activity.log'
OUTPUTS       = BASE_DIR / 'outputs'
QUEUE_F       = BASE_DIR / 'queue.json'
CONTACTS_F    = BASE_DIR / 'contacts_cache.json'
PIPELINE_F    = BASE_DIR / 'pipeline_data.json'
PORT          = 3737


def _load_env():
    env_file = BASE_DIR / '.env'
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                k, v = line.split('=', 1)
                os.environ.setdefault(k.strip(), v.strip())


_load_env()

MIXMAX_TOKEN  = os.environ.get('MIXMAX_TOKEN', '')
MIXMAX_SEQS   = [
    '6a048cfc110bc620ca0f1aee',  # Property Managers
    '6a048cfba81429e5dfe55010',  # Realtors
    '6a048cfd624a5989a68ba16c',  # Contractors
]
SEQ_LABELS    = {
    '6a048cfc110bc620ca0f1aee': {'name': 'Property Managers', 'type': 'property_manager'},
    '6a048cfba81429e5dfe55010': {'name': 'Realtors',          'type': 'realtor'},
    '6a048cfd624a5989a68ba16c': {'name': 'Contractors',       'type': 'contractor'},
}

INSTANTLY_KEY = os.environ.get('INSTANTLY_API_KEY', '')
INSTANTLY_CAMPAIGNS = {
    'a1c08c3d-43c6-4a0f-b253-e3f14e66f3bc': {'name': 'Property Managers — Cuyahoga County', 'worker': 'danny'},
    '626cd15d-4d89-4c29-a609-436e69fbb404': {'name': 'Referral Partners — Contractors NE Ohio', 'worker': 'carla'},
}

WORKERS = ['danny', 'carla', 'marcus', 'nina', 'tommy', 'jasmine', 'rick', 'donna']

LOG_RE = re.compile(r'\[(.+?)\]\s+(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+)')


def parse_log():
    if not LOG_FILE.exists():
        return []
    entries = []
    for line in LOG_FILE.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        m = LOG_RE.match(line)
        if m:
            entries.append({
                'timestamp':   m.group(1).strip(),
                'worker':      m.group(2).strip().lower(),
                'task':        m.group(3).strip(),
                'output_file': m.group(4).strip(),
                'status':      m.group(5).strip(),
            })
        else:
            # Store unparsed lines too so nothing is lost
            entries.append({'raw': line})
    return entries


def get_outputs():
    result = {}
    for w in WORKERS:
        d = OUTPUTS / w
        result[w] = sorted([f.name for f in d.iterdir() if f.is_file()], reverse=True) if d.exists() else []
    return result


def get_queue():
    if QUEUE_F.exists():
        return json.loads(QUEUE_F.read_text())
    return []


def save_queue(data):
    QUEUE_F.write_text(json.dumps(data, indent=2))


def get_contacts():
    if CONTACTS_F.exists():
        return json.loads(CONTACTS_F.read_text())
    return {'contacts': [], 'updated': 0}


def sync_contacts():
    """Pull latest leads from Instantly and cache locally."""
    import time
    all_contacts = []
    for cid, meta in INSTANTLY_CAMPAIGNS.items():
        try:
            payload = json.dumps({'campaign_id': cid, 'limit': 100}).encode()
            req = urllib.request.Request(
                'https://api.instantly.ai/api/v2/leads/list',
                data=payload,
                headers={'Authorization': f'Bearer {INSTANTLY_KEY}', 'Content-Type': 'application/json'},
                method='POST'
            )
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read())
            items = data.get('items', [])
            for item in items:
                item['_campaign_id'] = cid
                item['_campaign_name'] = meta['name']
                item['_worker'] = meta['worker']
            all_contacts.extend(items)
        except Exception:
            pass
    if all_contacts:
        CONTACTS_F.write_text(json.dumps({'contacts': all_contacts, 'updated': time.time()}, indent=2))


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(BASE_DIR), **kwargs)

    def log_message(self, *_):
        pass

    def _json(self, data, status=200):
        body = json.dumps(data).encode()
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_GET(self):
        p = urlparse(self.path)
        qs = parse_qs(p.query)

        if p.path == '/api/log':
            self._json(parse_log())
        elif p.path == '/api/outputs':
            self._json(get_outputs())
        elif p.path == '/api/file':
            worker = qs.get('worker', [''])[0]
            fname  = qs.get('file',   [''])[0]
            if worker in WORKERS and fname:
                fp = OUTPUTS / worker / fname
                if fp.exists() and fp.is_file():
                    self._json({'content': fp.read_text(), 'filename': fname, 'worker': worker})
                    return
            self._json({'error': 'not found'}, 404)
        elif p.path == '/api/queue':
            self._json(get_queue())
        elif p.path == '/api/contacts':
            self._json(get_contacts())
        elif p.path == '/api/contacts/sync':
            sync_contacts()
            self._json(get_contacts())
        elif p.path == '/api/mixmax/recipients':
            # Pull recipients from a single Mixmax sequence
            seq_id = qs.get('seq', [''])[0]
            if not seq_id:
                self._json({'error': 'missing seq param'}, 400)
                return
            try:
                url = f'https://api.mixmax.com/v1/sequences/{seq_id}/recipients?apiToken={MIXMAX_TOKEN}&limit=200'
                with urllib.request.urlopen(url, timeout=10) as resp:
                    data = json.loads(resp.read())
                self._json({'recipients': data if isinstance(data, list) else []})
            except Exception as e:
                self._json({'error': str(e)}, 500)

        elif p.path == '/api/apollo/linkedin':
            # Look up LinkedIn URL for a contact via Apollo people/match
            import subprocess
            email      = qs.get('email',      [''])[0]
            first_name = qs.get('first_name', [''])[0]
            company    = qs.get('company',    [''])[0]
            if not email:
                self._json({'linkedin_url': None})
                return
            try:
                payload = json.dumps({
                    'email': email,
                    'first_name': first_name,
                    'organization_name': company,
                    'reveal_personal_emails': False,
                })
                result = subprocess.run(
                    ['curl', '-s', '-X', 'POST',
                     'https://api.apollo.io/api/v1/people/match',
                     '-H', 'Content-Type: application/json',
                     '-H', 'X-Api-Key: aKRZyBffyV7ScWVCuTXBjA',
                     '-d', payload],
                    capture_output=True, text=True, timeout=10
                )
                data   = json.loads(result.stdout)
                person = data.get('person', {})
                self._json({'linkedin_url': person.get('linkedin_url')})
            except Exception as e:
                self._json({'linkedin_url': None, 'error': str(e)})

        elif p.path == '/api/mixmax/sequences':
            # Return all Mixmax sequences with recipient counts
            try:
                from integrations.mixmax import get_all_sequences, SEQUENCES
                seqs = get_all_sequences()
                # Tag which ones are ours
                our_ids = {v['id']: k for k, v in SEQUENCES.items()}
                for s in seqs:
                    s['_fc_type'] = our_ids.get(s['_id'], '')
                self._json({'sequences': seqs, 'our_sequences': SEQUENCES})
            except Exception as e:
                self._json({'error': str(e)}, 500)

        elif p.path == '/api/mixmax/enroll/all':
            # Enroll all contacts from cache into Mixmax sequences
            try:
                from integrations.mixmax import enroll_batch
                cache = get_contacts()
                contacts = cache.get('contacts', [])
                results = enroll_batch(contacts, skip_existing=True)
                # Save updated cache with mixmax_enrolled flags
                import time
                CONTACTS_F.write_text(json.dumps(
                    {'contacts': contacts, 'updated': time.time()}, indent=2
                ))
                self._json({
                    'enrolled': len(results['enrolled']),
                    'skipped':  len(results['skipped']),
                    'errors':   len(results['errors']),
                    'details':  results,
                })
            except Exception as e:
                self._json({'error': str(e)}, 500)

        elif p.path == '/api/pipeline':
            # Return merged pipeline: Mixmax recipients + local stage overrides
            import time as _time
            pipeline = json.loads(PIPELINE_F.read_text()) if PIPELINE_F.exists() else {}

            # Build phone + company lookup from contacts cache (email → {phone, company_name})
            cache_lookup = {}
            if CONTACTS_F.exists():
                cache_data = json.loads(CONTACTS_F.read_text())
                for cc in cache_data.get('contacts', []):
                    em = (cc.get('email') or '').lower()
                    if em:
                        cache_lookup[em] = {
                            'phone':   cc.get('phone', ''),
                            'company': cc.get('company_name') or cc.get('organization') or '',
                        }

            all_contacts = []
            for seq_id in MIXMAX_SEQS:
                try:
                    url = f'https://api.mixmax.com/v1/sequences/{seq_id}/recipients?apiToken={MIXMAX_TOKEN}&limit=200'
                    with urllib.request.urlopen(url, timeout=10) as resp:
                        recipients = json.loads(resp.read())
                    if not isinstance(recipients, list):
                        continue
                    for r in recipients:
                        email = (r.get('to') or {}).get('email', '').lower()
                        if not email:
                            continue
                        opens   = (r.get('analytics') or {}).get('events', {}).get('opens', 0)
                        clicks  = (r.get('analytics') or {}).get('events', {}).get('clicks', 0)
                        replied = sum(s.get('replied', 0) for s in r.get('stages', []))
                        saved   = pipeline.get(email, {})
                        cached  = cache_lookup.get(email, {})
                        # Auto-stage from Mixmax signals if no manual override
                        auto_stage = 'New Lead'
                        if replied > 0:
                            auto_stage = 'Replied'
                        elif r.get('state') == 'active':
                            auto_stage = 'Contacted'
                        stage = saved.get('stage', auto_stage)
                        last_contact = saved.get('last_contact', '')
                        # Stale detection
                        stale = False
                        if last_contact:
                            try:
                                from datetime import datetime as _dt
                                lc = _dt.strptime(last_contact, '%Y-%m-%d')
                                days = (_dt.now() - lc).days
                                thresholds = {'New Lead': 2, 'Contacted': 5, 'Replied': 2, 'Estimate Sent': 3, 'Follow-Up': 5}
                                stale = days >= thresholds.get(stage, 5)
                            except Exception:
                                pass
                        all_contacts.append({
                            'email':        email,
                            'phone':        cached.get('phone', ''),
                            'name':         (r.get('to') or {}).get('name', ''),
                            'company':      saved.get('company', '') or cached.get('company', ''),
                            'sequence':     SEQ_LABELS[seq_id]['name'],
                            'lead_type':    SEQ_LABELS[seq_id]['type'],
                            'stage':        stage,
                            'opens':        opens,
                            'clicks':       clicks,
                            'replied':      replied > 0,
                            'last_contact': last_contact,
                            'next_followup': saved.get('next_followup', ''),
                            'est_value':    saved.get('est_value', ''),
                            'notes':        saved.get('notes', ''),
                            'stale':        stale,
                        })
                except Exception:
                    continue

            # Include manually imported contacts from pipeline_data.json
            calls_data = pipeline.get('calls', {})
            for mc in pipeline.get('manual_contacts', []):
                stage       = mc.get('stage', 'New Lead')
                last_contact = mc.get('last_contact', '')
                # Fall back to calls log for last_contact so stale detection works
                if not last_contact:
                    call_entry = calls_data.get(mc.get('id', ''), {})
                    last_contact = call_entry.get('called_at', '')
                stale = False
                if last_contact:
                    try:
                        from datetime import datetime as _dt
                        lc = _dt.strptime(last_contact, '%Y-%m-%d')
                        days = (_dt.now() - lc).days
                        thresholds = {'New Lead': 2, 'Contacted': 5, 'Replied': 2, 'Estimate Sent': 3, 'Follow-Up': 5}
                        stale = days >= thresholds.get(stage, 5)
                    except Exception:
                        pass
                name = ' '.join(filter(None, [mc.get('first_name',''), mc.get('last_name','')])).strip()
                all_contacts.append({
                    'id':           mc.get('id', ''),
                    'email':        mc.get('email', ''),
                    'phone':        mc.get('phone', ''),
                    'name':         name,
                    'company':      mc.get('company', ''),
                    'sequence':     'Manual Import',
                    'lead_type':    mc.get('lead_type', 'contractor'),
                    'stage':        stage,
                    'opens':        0,
                    'clicks':       0,
                    'replied':      stage in ('Replied', 'Meeting Set', 'Estimate Sent', 'Closed Won'),
                    'last_contact': last_contact,
                    'next_followup': mc.get('next_followup', ''),
                    'est_value':    mc.get('est_value', ''),
                    'notes':        mc.get('notes', ''),
                    'stale':        stale,
                    'source':       'manual',
                })
            self._json({'contacts': all_contacts, 'total': len(all_contacts)})

        elif p.path == '/api/calls':
            pipeline = json.loads(PIPELINE_F.read_text()) if PIPELINE_F.exists() else {}
            self._json(pipeline.get('calls', {}))

        elif p.path.startswith('/api/instantly/'):
            # Proxy to Instantly API — avoids CORS issues from browser
            auth = self.headers.get('Authorization', '')
            instantly_path = p.path.replace('/api/instantly/', '')
            url = f'https://api.instantly.ai/api/v2/{instantly_path}'
            if p.query:
                url += '?' + p.query
            try:
                req = urllib.request.Request(url, headers={
                    'Authorization': auth,
                    'Content-Type': 'application/json'
                })
                with urllib.request.urlopen(req, timeout=10) as resp:
                    body = resp.read()
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Content-Length', str(len(body)))
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(body)
            except urllib.error.HTTPError as e:
                body = e.read()
                self.send_response(e.code)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(body)
            except Exception as e:
                self._json({'error': str(e)}, 500)
        else:
            super().do_GET()

    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        body   = self.rfile.read(length)

        if self.path == '/api/queue':
            save_queue(json.loads(body))
            self._json({'ok': True})

        elif self.path == '/api/mixmax/enroll':
            # Enroll a single lead: POST { email, first_name, last_name, company_name, title, phone, _worker }
            try:
                from integrations.mixmax import enroll_lead
                lead = json.loads(body)
                result = enroll_lead(lead)
                # Update contacts cache if enrolled
                if result.get('status') == 'enrolled':
                    import time
                    cache = get_contacts()
                    contacts = cache.get('contacts', [])
                    for c in contacts:
                        if c.get('email', '').lower() == lead.get('email', '').lower():
                            c['mixmax_enrolled'] = True
                            c['mixmax_sequence'] = result.get('sequence', '')
                            c['mixmax_lead_type'] = result.get('lead_type', '')
                    CONTACTS_F.write_text(json.dumps(
                        {'contacts': contacts, 'updated': time.time()}, indent=2
                    ))
                self._json(result)
            except Exception as e:
                self._json({'error': str(e)}, 500)

        elif self.path == '/api/pipeline':
            # Save stage/notes update for a contact
            try:
                data  = json.loads(body)
                email = data.get('email', '').lower()
                if not email:
                    self._json({'error': 'missing email'}, 400)
                    return
                pipeline = json.loads(PIPELINE_F.read_text()) if PIPELINE_F.exists() else {}
                if email not in pipeline:
                    pipeline[email] = {}
                for field in ('stage', 'notes', 'last_contact', 'next_followup', 'est_value', 'company'):
                    if field in data:
                        pipeline[email][field] = data[field]
                PIPELINE_F.write_text(json.dumps(pipeline, indent=2))
                self._json({'ok': True, 'email': email})
            except Exception as e:
                self._json({'error': str(e)}, 500)

        elif self.path == '/api/calls':
            # Save call status: POST { key, called, notes }
            try:
                data = json.loads(body)
                key   = data.get('key', '')
                if not key:
                    self._json({'error': 'missing key'}, 400)
                    return
                pipeline = json.loads(PIPELINE_F.read_text()) if PIPELINE_F.exists() else {}
                if 'calls' not in pipeline:
                    pipeline['calls'] = {}
                pipeline['calls'][key] = {
                    'called':    data.get('called', True),
                    'called_at': data.get('called_at', ''),
                    'notes':     data.get('notes', ''),
                }
                PIPELINE_F.write_text(json.dumps(pipeline, indent=2))
                self._json({'ok': True, 'key': key})
            except Exception as e:
                self._json({'error': str(e)}, 500)

        elif self.path == '/api/contacts/workflow':
            # Update workflow checklist for a contact: POST { email, step, done }
            try:
                import time
                data = json.loads(body)
                email = data.get('email', '').lower()
                step  = data.get('step', '')
                done  = data.get('done', True)
                cache = get_contacts()
                contacts = cache.get('contacts', [])
                updated = False
                for c in contacts:
                    if c.get('email', '').lower() == email:
                        if 'workflow' not in c:
                            c['workflow'] = {}
                        c['workflow'][step] = done
                        updated = True
                if updated:
                    CONTACTS_F.write_text(json.dumps(
                        {'contacts': contacts, 'updated': time.time()}, indent=2
                    ))
                self._json({'ok': updated, 'email': email, 'step': step, 'done': done})
            except Exception as e:
                self._json({'error': str(e)}, 500)

        else:
            self.send_response(404)
            self.end_headers()


if __name__ == '__main__':
    import webbrowser, threading
    url = f'http://localhost:{PORT}/dashboard.html'
    print(f'\n  Forest City AI Office')
    print(f'  Dashboard → {url}')
    print(f'  Press Ctrl+C to stop\n')
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(('', PORT), Handler) as httpd:
        threading.Timer(1.0, lambda: webbrowser.open(url)).start()
        httpd.serve_forever()
