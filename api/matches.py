import json
from http.server import BaseHTTPRequestHandler
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))
from football_api import FootballAPI

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        api = FootballAPI()
        data = api.get_live_matches()
        
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache')
        self.end_headers()
        self.wfile.write(json.dumps(data, indent=2).encode('utf-8'))
    
    def log_message(self, format, *args):
        pass
