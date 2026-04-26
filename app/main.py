from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from datetime import datetime
import json
import os

PORT = 7000
LOG_FILE = "logs/final_service.log"

def write_log(level, message):
    os.makedirs("logs", exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} {level} {message}\n")

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            data = {"message": "hello final service"}
            status = 200
            write_log("INFO", "GET /")
        elif self.path == "/health":
            data = {"status": "ok"}
            status = 200
            write_log("INFO", "GET /health")
        elif self.path == "/version":
            data = {"version": "1.0.0"}
            status = 200
            write_log("INFO", "GET /version")
        elif self.path == "/error":
            data = {"error": "fake error"}
            status = 500
            write_log("ERROR", "GET /error")
        else:
            data = {"error": "not found"}
            status = 404
            write_log("WARNING", f"unknown path {self.path}")

        body = (json.dumps(data, ensure_ascii=False) + "\n").encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(body)

write_log("INFO", f"service starting on port {PORT}")
server = ThreadingHTTPServer(("0.0.0.0", PORT), Handler)
print(f"Final service running on port {PORT}")
server.serve_forever()
