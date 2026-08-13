from http.server import BaseHTTPRequestHandler
import requests
import json
import urllib.parse as urlparse

# 🔗 Original API
BASE_API = "https://yash-code-with-ai.alphamovies.workers.dev/"

# 🔑 Hidden API key
API_KEY = "7189814021"

# 👑 Your Details & Customization
OWNER_NAME = "𝐅𝐫𝐞𝐱𝐱𝐲"
PROJECT_NAME = "𝐅𝐫𝐞𝐱𝐱𝐲"

def format_and_sort_data(data):
    priority_keys = [
        "api_name", "NAME", "name", "FNAME", "fname", 
        "MOBILE", "mobile", "ALT", "alt", "ID", "id", 
        "ADDRESS", "address", "CIRCLE", "circle",
        "owner_contact", "branding", "developer", "processed_by", "powered_by", "api_owner"
    ]
    
    if isinstance(data, dict):
        sorted_data = {}
        for key in priority_keys:
            if key in data:
                sorted_data[key] = format_and_sort_data(data[key])
        for key, value in data.items():
            if key not in sorted_data:
                sorted_data[key] = format_and_sort_data(value)
        return sorted_data
    elif isinstance(data, list):
        return [format_and_sort_data(item) for item in data]
    else:
        return data

def generate_html_output(data, project_name, owner):
    """Ye function JSON data ko ek colorful, professional dark-mode HTML UI me convert karega"""
    
    # JSON data ko pretty format me convert karna
    pretty_json = json.dumps(data, indent=4, ensure_ascii=False)
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{project_name} - Dashboard</title>
        <style>
            body {{
                background-color: #0b0f19;
                color: #00ff66;
                font-family: 'Courier New', Courier, monospace;
                margin: 0;
                padding: 20px;
            }}
            .container {{
                max-width: 800px;
                margin: auto;
                background: #111827;
                border: 2px solid #00ff66;
                border-radius: 10px;
                box-shadow: 0 0 20px rgba(0, 255, 102, 0.3);
                padding: 20px;
            }}
            h0, h1 {{
                text-align: center;
                color: #00ffff;
                text-shadow: 0 0 10px rgba(0, 255, 255, 0.5);
            }}
            .badge {{
                background: #1f2937;
                color: #ff00ff;
                padding: 5px 10px;
                border-radius: 5px;
                font-weight: bold;
                display: inline-block;
                margin-bottom: 15px;
            }}
            pre {{
                background: #000000;
                color: #00ff66;
                padding: 15px;
                border-radius: 5px;
                border: 1px solid #374151;
                overflow-x: auto;
                font-size: 14px;
                line-height: 1.5;
            }}
            .footer {{
                text-align: center;
                margin-top: 20px;
                color: #9ca3af;
                font-size: 12px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>⚡ {project_name} ⚡</h1>
            <div style="text-align: center;">
                <span class="badge">Powered by: {owner}</span>
            </div>
            <p>🔥 <b>Status:</b> Online & Working Successfully</p>
            <h3>📁 Response Data (OSINT Result):</h3>
            <pre>{pretty_json}</pre>
            <div class="footer">
                &copy; 2026 {project_name} | Created by {owner}
            </div>
        </div>
    </body>
    </html>
    """
    return html_content

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            query = urlparse.urlparse(self.path).query
            params = urlparse.parse_qs(query)

            number = params.get("num", [""])[0]

            if not number:
                raise Exception("Number missing! Use format: /?num=YOUR_NUMBER")

            # 🔗 Call original API
            url = f"{BASE_API}?num={number}&key={API_KEY}"
            res = requests.get(url, timeout=10)
            
            if res.status_code == 200:
                data = res.json()
            else:
                raise Exception("Original API se response nahi mila")

            # 🔥 ADD CUSTOM BRANDING FIELDS
            if isinstance(data, dict):
                data["api_name"] = PROJECT_NAME
                data["owner_contact"] = f"@{OWNER_NAME}"
                data["branding"] = OWNER_NAME
                data["developer"] = OWNER_NAME
                data["processed_by"] = OWNER_NAME
                data["powered_by"] = OWNER_NAME
                data["api_owner"] = OWNER_NAME

            # 🔄 REORDER KEYS STEP BY STEP
            final_data = format_and_sort_data(data)

            # Check karo ki user browser se aaya hai ya code/bot se
            accept_header = self.headers.get("Accept", "")
            
            if "text/html" in accept_header:
                # Agar browser se khola hai toh Colorful HTML UI dikhao
                self.send_response(200)
                self.send_header("Content-type", "text/html; charset=utf-8")
                self.end_headers()
                html_output = generate_html_output(final_data, PROJECT_NAME, OWNER_NAME)
                self.wfile.write(html_output.encode('utf-8'))
            else:
                # Agar bot ya script se request hai toh JSON return karo
                self.send_response(200)
                self.send_header("Content-type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps(final_data, ensure_ascii=False).encode('utf-8'))

        except Exception as e:
            error_response = {"error": str(e)}
            self.send_response(500)
            self.send_header("Content-type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(error_response, ensure_ascii=False).encode('utf-8'))
