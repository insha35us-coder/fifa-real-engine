import json
from datetime import datetime
from http.server import BaseHTTPRequestHandler

# Simple in-memory storage (use database in production)
clicks_db = []
earnings_db = []

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Track click
        click_data = {
            "timestamp": datetime.now().isoformat(),
            "tag": "timevalue0e2-20",
            "ip": self.client_address[0],
            "user_agent": self.headers.get('User-Agent', 'Unknown')
        }
        clicks_db.append(click_data)
        
        # Calculate earnings (estimated)
        today = datetime.now().date()
        today_clicks = [c for c in clicks_db if c['timestamp'].startswith(str(today))]
        
        # Amazon average conversion: 1 sale per 100 clicks
        # Average commission: $40
        estimated_sales = len(today_clicks) // 100
        estimated_earnings = estimated_sales * 40
        
        response = {
            "status": "tracked",
            "total_clicks_today": len(today_clicks),
            "estimated_sales": estimated_sales,
            "estimated_earnings": f"${estimated_earnings}",
            "affiliate_tag": "timevalue0e2-20",
            "real_time": True
        }
        
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(response, indent=2).encode('utf-8'))
    
    def log_message(self, format, *args):
        pass
