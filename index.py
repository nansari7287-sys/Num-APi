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
PROJECT_NAME = "𝑫𝒓𝒂𝒌𝒐𝑿𝑵𝒂𝒆𝒆𝒎"

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
    """Neon Theme Hacker UI for Web Browser with Image Background"""
    
    pretty_json = json.dumps(data, indent=4, ensure_ascii=False)
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{project_name} - Advanced System</title>
        <style>
            body {{
                background: url('1000324185.png') no-repeat center center fixed;
                background-size: cover;
                color: #e0b0ff;
                font-family: 'Courier New', Courier, monospace;
                margin: 0;
                padding: 20px;
            }}
            .container {{
                max-width: 850px;
                margin: auto;
                background: rgba(10, 10, 20, 0.75);
                border: 2px solid #bc13fe;
                border-radius: 15px;
                box-shadow: 0 0 25px rgba(188, 19, 254, 0.6);
                backdrop-filter: blur(8px);
                padding: 25px;
            }}
            h1 {{
                text-align: center;
                color: #ff00ff;
                text-transform: uppercase;
                letter-spacing: 2px;
                text-shadow: 0 0 10px #ff00ff, 0 0 20px #bc13fe, 0 0 40px #bc13fe;
            }}
            .badge {{
                background: rgba(20, 20, 30, 0.9);
                color: #00ffff;
                padding: 8px 15px;
                border-radius: 8px;
                font-weight: bold;
                display: inline-block;
                margin-bottom: 20px;
                box-shadow: 0 0 10px rgba(0, 255, 255, 0.4);
                border: 1px solid #00ffff;
            }}
            .status {{
                color: #00ff66;
                text-shadow: 0 0 10px rgba(0, 255, 102, 0.7);
                font-weight: bold;
                font-size: 1.1em;
            }}
            pre {{
                background: rgba(0, 0, 0, 0.8);
                color: #00ff66;
                padding: 20px;
                border-radius: 10px;
                border: 1px solid #bc13fe;
                box-shadow: inset 0 0 15px rgba(188, 19, 254, 0.3);
                overflow-x: auto;
                font-size: 15px;
                line-height: 1.6;
            }}
            .footer {{
                text-align: center;
                margin-top: 25px;
                color: #d1d5db;
                font-size: 13px;
                text-shadow: 0 0 5px #ffffff;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>⚡ {project_name} ⚡</h1>
            <div style="text-align: center;">
                <span class="badge">Powered by: {owner}</span>
            </div>
            <p class="status">🔥 [ SYSTEM STATUS ]: ONLINE & ENCRYPTED</p>
            <h3 style="color: #bc13fe; text-shadow: 0 0 5px #bc13fe;">📁 Extracted Data Payload:</h3>
            <pre>{pretty_json}</pre>
            <div class="footer">
                &copy; 2026 {project_name} | Secured by {owner}
            </div>
        </div>
    </body>
    </html>
    """
    return html_content

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Serve the background image if requested by the browser
            if self.path.endswith("1000324185.png"):
                try:
                    with open("1000324185.png", "rb") as f:
                        self.send_response(200)
                        self.send_header("Content-type", "image/png")
                        self.end_headers()
                        self.wfile.write(f.read())
                    return
                except FileNotFoundError:
                    self.send_response(404)
                    self.end_headers()
                    return

            query = urlparse.urlparse(self.path).query
            params = urlparse.parse_qs(query)

            number = params.get("num", [""])[0]

            if not number:
                raise Exception("System Error: Number missing! Use format: /?num=TARGET_NUMBER")

            # 🔗 Call original API
            url = f"{BASE_API}?num={number}&key={API_KEY}"
            res = requests.get(url, timeout=10)
            
            if res.status_code == 200:
                data = res.json()
            else:
                raise Exception("Original Server Offline")

            # 🔥 MODIFY RESPONSE
            if isinstance(data, dict):
                data["api_name"] = PROJECT_NAME
                data["owner_contact"] = f"@{OWNER_NAME}"
                data["branding"] = OWNER_NAME
                data["developer"] = OWNER_NAME
                data["processed_by"] = OWNER_NAME
                data["powered_by"] = OWNER_NAME
                data["api_owner"] = OWNER_NAME

            final_data = format_and_sort_data(data)

            accept_header = self.headers.get("Accept", "")
            
            if "text/html" in accept_header:
                self.send_response(200)
                self.send_header("Content-type", "text/html; charset=utf-8")
                self.end_headers()
                html_output = generate_html_output(final_data, PROJECT_NAME, OWNER_NAME)
                self.wfile.write(html_output.encode('utf-8'))
            else:
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
