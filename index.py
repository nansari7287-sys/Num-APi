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
PROJECT_NAME = "𝑫𝒓𝒂𝒌𝒐𝑿𝑵𝒂𝒆𝒆𝒎 API"

def generate_html_output(final_data, new_records):
    """Premium Hacker Terminal UI Generator"""
    
    records_html = ""
    if not new_records:
        records_html = "<div class='record-box' style='text-align:center; color:#ff003c;'>❌ No Data Found For This Number ❌</div>"
    else:
        for idx, rec in enumerate(new_records):
            records_html += f"""
            <div class="record-box">
                <div class="record-title">▼▼ [ RECORD {idx + 1} ] ▼▼</div>
                <table class="data-table">
                    <tr><td class="key">NAME</td><td class="value">: {rec.get('NAME', 'N/A')}</td></tr>
                    <tr><td class="key">FNAME</td><td class="value">: {rec.get('FNAME', 'N/A')}</td></tr>
                    <tr><td class="key">MOBILE</td><td class="value">: {rec.get('MOBILE', 'N/A')}</td></tr>
                    <tr><td class="key">ID</td><td class="value">: {rec.get('ID', 'N/A')}</td></tr>
                    <tr><td class="key">ADDRESS</td><td class="value">: {rec.get('ADDRESS', 'N/A')}</td></tr>
                    <tr><td class="key">CIRCLE</td><td class="value">: {rec.get('CIRCLE', 'N/A')}</td></tr>
                </table>
            </div>
            """

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{PROJECT_NAME} - Advanced System</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');
            body {{
                /* Added / before image name to fix Vercel path issue */
                background: url('/1000324185.png') no-repeat center center fixed, #0b0c10;
                background-size: cover;
                color: #e0b0ff;
                font-family: 'Share Tech Mono', 'Courier New', monospace;
                margin: 0;
                padding: 15px;
            }}
            .container {{
                max-width: 800px;
                margin: 20px auto;
                background: rgba(10, 10, 15, 0.85);
                border: 1px solid #bc13fe;
                border-radius: 12px;
                box-shadow: 0 0 30px rgba(188, 19, 254, 0.4), inset 0 0 15px rgba(188, 19, 254, 0.2);
                backdrop-filter: blur(10px);
                padding: 25px;
                position: relative;
                overflow: hidden;
            }}
            .container::before {{
                content: "";
                position: absolute;
                top: 0; left: 0; right: 0; height: 3px;
                background: linear-gradient(90deg, transparent, #ff00ff, #00ffff, transparent);
                animation: scanline 3s linear infinite;
            }}
            @keyframes scanline {{
                0% {{ transform: translateX(-100%); }}
                100% {{ transform: translateX(100%); }}
            }}
            h1 {{
                text-align: center;
                color: #fff;
                text-shadow: 0 0 10px #ff00ff, 0 0 20px #bc13fe;
                font-size: 32px;
                margin-top: 0;
            }}
            .branding {{
                text-align: center;
                margin-bottom: 30px;
            }}
            .badge {{
                background: rgba(188, 19, 254, 0.1);
                color: #00ffff;
                padding: 8px 20px;
                border: 1px solid #00ffff;
                border-radius: 20px;
                font-size: 16px;
                box-shadow: 0 0 10px rgba(0, 255, 255, 0.2);
                text-transform: uppercase;
                letter-spacing: 1px;
            }}
            .terminal-header {{
                color: #00ff66;
                text-shadow: 0 0 8px rgba(0, 255, 102, 0.6);
                font-size: 18px;
                margin-bottom: 20px;
                text-align: center;
                border-bottom: 1px dashed #00ff66;
                padding-bottom: 10px;
            }}
            .record-box {{
                background: rgba(0, 0, 0, 0.7);
                border: 1px solid #00ff66;
                border-left: 5px solid #00ff66;
                margin-bottom: 20px;
                padding: 15px;
                border-radius: 6px;
                box-shadow: 0 4px 15px rgba(0, 255, 102, 0.1);
            }}
            .record-title {{
                color: #ffff00;
                font-weight: bold;
                font-size: 18px;
                margin-bottom: 12px;
                text-shadow: 0 0 8px rgba(255, 255, 0, 0.5);
            }}
            .data-table {{
                width: 100%;
                border-collapse: collapse;
            }}
            .data-table td {{
                padding: 6px 0;
                vertical-align: top;
                font-size: 16px;
            }}
            .key {{
                color: #00ffff;
                width: 120px;
                font-weight: bold;
            }}
            .value {{
                color: #00ff66;
                word-break: break-word;
            }}
            .footer {{
                text-align: center;
                margin-top: 30px;
                color: #888;
                font-size: 13px;
                border-top: 1px solid #333;
                padding-top: 15px;
            }}
            .footer span {{
                color: #bc13fe;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🌌 {PROJECT_NAME} 🌌</h1>
            <div class="branding">
                <span class="badge">Powered By: {OWNER_NAME}</span>
            </div>
            
            <div class="terminal-header">
                🔥 [ SYSTEM STATUS ]: ONLINE & SECURED 🔥<br><br>
                ▼▼ [ NUMBER INFO DETAILS ] ▼▼
            </div>
            
            <div class="records">
                {records_html}
            </div>

            <div class="footer">
                &copy; 2026 <span>{PROJECT_NAME}</span> | Advanced Data Extraction System
            </div>
        </div>
    </body>
    </html>
    """
    return html_content

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # 📸 Background image loading fix
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
                original_data = res.json()
            else:
                raise Exception("Original Server Offline")

            # 🔥 RESTRUCTURE DATA (Sasta data ko premium step-by-step me convert karna)
            new_records = []
            if "data" in original_data and isinstance(original_data["data"], list):
                for record in original_data["data"]:
                    # Exact sequence set kar rahe hain yahan
                    new_record = {
                        "NAME": record.get("full_name", record.get("name", "")),
                        "FNAME": record.get("the_name_of_the_father", record.get("fname", "")),
                        "MOBILE": record.get("phone", record.get("mobile", "")),
                        "ID": record.get("document_number", record.get("id", "")),
                        "ADDRESS": record.get("address", ""),
                        "CIRCLE": record.get("region", record.get("circle", ""))
                    }
                    # Khali (empty) fields ko hide karne ke liye
                    clean_record = {k: v for k, v in new_record.items() if v != ""}
                    new_records.append(clean_record)

            final_data = {
                "api_name": PROJECT_NAME,
                "owner_contact": f"@{OWNER_NAME}",
                "branding": OWNER_NAME,
                "developer": OWNER_NAME,
                "processed_by": OWNER_NAME,
                "powered_by": OWNER_NAME,
                "api_owner": OWNER_NAME,
                "status": original_data.get("status", "success"),
                "results_count": original_data.get("results_count", len(new_records)),
                "data": new_records
            }

            accept_header = self.headers.get("Accept", "")
            
            if "text/html" in accept_header:
                # Agar Browser se khola hai to Premium UI
                self.send_response(200)
                self.send_header("Content-type", "text/html; charset=utf-8")
                self.end_headers()
                html_output = generate_html_output(final_data, new_records)
                self.wfile.write(html_output.encode('utf-8'))
            else:
                # Agar Code/Bot se khola hai to Step-by-Step Clean JSON
                self.send_response(200)
                self.send_header("Content-type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps(final_data, indent=4, ensure_ascii=False).encode('utf-8'))

        except Exception as e:
            error_response = {"error": str(e)}
            self.send_response(500)
            self.send_header("Content-type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(error_response, ensure_ascii=False).encode('utf-8'))
