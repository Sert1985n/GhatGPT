import os, shutil, subprocess, html
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
PORT = int(os.environ.get('MONITOR_PORT','3420'))
def read(path):
    try:
        with open(path,'r',encoding='utf-8',errors='ignore') as f: return f.read()
    except Exception: return ''
def meminfo():
    data={}
    for line in read('/host/proc/meminfo').splitlines():
        if ':' in line:
            k,v=line.split(':',1); data[k]=int(v.strip().split()[0])
    total=data.get('MemTotal',0); avail=data.get('MemAvailable',0); used=max(total-avail,0)
    return total//1024, used//1024, avail//1024
def loadavg():
    s=read('/host/proc/loadavg').strip().split(); return ' '.join(s[:3]) if s else '-'
def disk():
    try:
        du=shutil.disk_usage('/host/root'); return round(du.total/1024**3,1), round(du.used/1024**3,1), round(du.free/1024**3,1), round(du.used*100/du.total,1)
    except Exception: return 0,0,0,0
def gpu():
    cmd=['nvidia-smi','--query-gpu=name,utilization.gpu,memory.used,memory.total,temperature.gpu,power.draw','--format=csv,noheader,nounits']
    try:
        out=subprocess.check_output(cmd, text=True, stderr=subprocess.STDOUT, timeout=5); rows=[]
        for line in out.strip().splitlines():
            parts=[p.strip() for p in line.split(',')]
            if len(parts)>=6: rows.append({'name':parts[0], 'util':parts[1], 'mem_used':parts[2], 'mem_total':parts[3], 'temp':parts[4], 'power':parts[5]})
        return rows
    except Exception:
        return [{'name':'nvidia-smi unavailable','util':'-','mem_used':'-','mem_total':'-','temp':'-','power':'-'}]
def containers(): return 'docker.sock mounted' if os.path.exists('/var/run/docker.sock') else 'docker.sock not mounted'
class H(BaseHTTPRequestHandler):
    def do_GET(self):
        mt,mu,ma=meminfo(); dt,du,df,dp=disk(); g=gpu(); la=loadavg()
        gpu_cards=''.join(["<div class=card><h3>GPU %d</h3><b>%s</b><p>load: %s%%<br>mem: %s / %s MB<br>temp: %s C<br>power: %s W</p></div>" % (i+1, html.escape(x['name']), x['util'], x['mem_used'], x['mem_total'], x['temp'], x['power']) for i,x in enumerate(g)])
        mem_pct=round(mu*100/mt,1) if mt else 0
        body=("<!doctype html><html><head><meta charset=utf-8><title>GhatGPT Monitor 3420</title><meta http-equiv=refresh content=5><style>"
        "body{margin:0;background:#05070b;color:#e5e7eb;font-family:Arial,sans-serif}header{padding:24px 28px;border-bottom:1px solid #1f2937}h1{margin:0;font-size:28px}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px;padding:20px}.card{background:#0f172a;border:1px solid #263244;border-radius:18px;padding:18px}b{color:#fff}.num{font-size:34px;color:#38bdf8;font-weight:700}p{line-height:1.65}</style></head><body>"
        "<header><h1>GhatGPT Monitor 3420</h1><div>online - refresh 5s</div></header><main class=grid>"
        f"<div class=card><h3>Processor</h3><div class=num>{html.escape(la)}</div><p>load average</p></div>"
        f"<div class=card><h3>Memory</h3><div class=num>{mem_pct}%</div><p>used: {mu} MB<br>total: {mt} MB<br>free: {ma} MB</p></div>"
        f"<div class=card><h3>Disk</h3><div class=num>{dp}%</div><p>used: {du} GB<br>free: {df} GB<br>total: {dt} GB</p></div>"
        f"<div class=card><h3>Containers</h3><p>{containers()}</p></div>" + gpu_cards + "</main></body></html>")
        self.send_response(200); self.send_header('Content-Type','text/html; charset=utf-8'); self.end_headers(); self.wfile.write(body.encode())
    def log_message(self,*args): pass
ThreadingHTTPServer(('0.0.0.0', PORT), H).serve_forever()
