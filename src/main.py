import http.server
import socketserver
import dotenv
import os

dotenv.load_dotenv()

PORT = int(os.environ.get("PORT", 8080))

class HelloWorldHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello, World!")

def main():
    with socketserver.TCPServer(("", PORT), HelloWorldHandler) as httpd:
        print(f"Serving on port {PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    main()
