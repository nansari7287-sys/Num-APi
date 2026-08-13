from http.server import BaseHTTPRequestHandler
import requests
import json
import urllib.parse as urlparse

# 🔗 Original API
BASE_API = "https://yash-code-with-ai.alphamovies.workers.dev/"

# 🔑 Hidden API key
API_KEY = "7189814021"

# 👑 Your Details
OWNER_NAME = "𝐅𝐫𝐞𝐱𝐱𝐲"
PROJECT_NAME = "𝐅𝐫𝐞𝐱𝐱𝐲"

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            query = urlparse.urlparse(self.path).query
            params = urlparse.parse_qs(query)

            number = params.get("num", [""])[0]

            if not number:
                raise Exception("Number missing")

            # 🔗 Call original API
            url = f"{BASE_API}?num={number}&key={API_KEY}"
            res = requests.get(url, timeout=10)
            
            if res.status_code == 200:
                data = res.json()
            else:
                raise Exception("Original API se response nahi mila")

            # 🔥 MODIFY RESPONSE (OWNER CHANGE)
            data["api_name"] = PROJECT_NAME
            data["owner_contact"] = f"@{OWNER_NAME}"
            data["branding"] = OWNER_NAME
            data["developer"] = OWNER_NAME
            data["processed_by"] = OWNER_NAME
            data["powered_by"] = OWNER_NAME
            data["api_owner"] = OWNER_NAME

            # Response send karna
            self.send_response(200)
            self.send_header("Content-type", "application/json; charset=utf-8")
            self.end_headers()
            
            self.wfile.write(json.dumps(data, ensure_ascii=False).encode('utf-8'))

        except Exception as e:
            self.send_response(500)
            self.send_header("Content-type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}, ensure_ascii=False).encode('utf-8'))
