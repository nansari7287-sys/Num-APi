from http.server import BaseHTTPRequestHandler
import requests
import json
import urllib.parse as urlparse

# 🔗 Original API
BASE_API = "https://yash-code-with-ai.alphamovies.workers.dev/"

# 🔑 Hidden API key
API_KEY = "7189814021"

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
            data = res.json()

            # 🔥 MODIFY RESPONSE (OWNER CHANGE)
            data["owner_contact"] = "@DarkOwnerX4"
            data["branding"] = "@DarkOwnerX4"
            data["developer"] = "@DarkOwnerX4"
            data["processed_by"] = "@DarkOwnerX4"

            # ➕ Extra custom field
            data["api_owner"] = "DarkOwnerX4"

            # OPTIONAL: clean unwanted fields
            # del data["owner_contact"]

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())

        except Exception as e:
            self.send_response(500)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())