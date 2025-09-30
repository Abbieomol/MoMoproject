import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import re
import base64

# --- CREDENTIALS ---
USERNAME = "admin"
PASSWORD = "password123"

# Load transactions
with open("data/processed/dashboard.json", "r") as f:
    transactions = json.load(f)
    
next_id = max(int(t["id"]) for t in transactions) + 1 if transactions else 1


class RequestHandler(BaseHTTPRequestHandler):
    def _send_json(self, data, code=200):
        self.send_response(code)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def _unauthorized(self):
        self.send_response(401)
        self.send_header("WWW-Authenticate", 'Basic realm="MoMo API"')
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"error": "Unauthorized"}).encode())

    def _check_auth(self):
        auth = self.headers.get('Authorization')
        if not auth or not auth.startswith('Basic '):
            return False
        try:
            encoded_credentials = auth.split(' ')[1]
            decoded = base64.b64decode(encoded_credentials).decode('utf-8')
            username, password = decoded.split(':')
            return username == USERNAME and password == PASSWORD
        except:
            return False

    def _parse_id(self, path):
        match = re.match(r"/transactions/(\d+)", path)
        return int(match.group(1)) if match else None

    def do_GET(self):
        if not self._check_auth():
            self._unauthorized()
            return

        if self.path == "/transactions":
            self._send_json(transactions)
        elif self.path.startswith("/transactions/"):
            tid = self._parse_id(self.path)
            for t in transactions:
                if t["id"] == tid:
                    self._send_json(t)
                    return
            self._send_json({"error": "Transaction not found"}, code=404)
        else:
            self._send_json({"error": "Endpoint not found"}, code=404)

    def do_POST(self):
        if not self._check_auth():
            self._unauthorized()
            return

        if self.path == "/transactions":
            content_length = int(self.headers.get("Content-Length", 0))
            post_data = self.rfile.read(content_length)
            new_transaction = json.loads(post_data)
            global next_id
            new_transaction["id"] = next_id
            next_id += 1
            transactions.append(new_transaction)
            self._send_json(new_transaction, code=201)
        else:
            self._send_json({"error": "Endpoint not found"}, code=404)

    def do_PUT(self):
        if not self._check_auth():
            self._unauthorized()
            return

        if self.path.startswith("/transactions/"):
            tid = self._parse_id(self.path)
            content_length = int(self.headers.get("Content-Length", 0))
            put_data = json.loads(self.rfile.read(content_length))
            for i, t in enumerate(transactions):
                if t["id"] == tid:
                    transactions[i].update(put_data)
                    self._send_json(transactions[i])
                    return
            self._send_json({"error": "Transaction not found"}, code=404)
        else:
            self._send_json({"error": "Endpoint not found"}, code=404)

    def do_DELETE(self):
        if not self._check_auth():
            self._unauthorized()
            return

        if self.path.startswith("/transactions/"):
            tid = self._parse_id(self.path)
            for i, t in enumerate(transactions):
                if t["id"] == tid:
                    deleted = transactions.pop(i)
                    self._send_json(deleted)
                    return
            self._send_json({"error": "Transaction not found"}, code=404)
        else:
            self._send_json({"error": "Endpoint not found"}, code=404)

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting secure server at http://localhost:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
