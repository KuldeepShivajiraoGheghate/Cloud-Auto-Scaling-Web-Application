from http.server import HTTPServer, BaseHTTPRequestHandler
import socket
import datetime

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        hostname = socket.gethostname()
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        body = f"""
        <html>
        <head><title>Auto Scaling Demo</title></head>
        <body style="font-family:sans-serif; padding:40px; background:#f0f4f8">
            <h1>Cloud Auto Scaling Web App</h1>
            <p><strong>Instance hostname:</strong> {hostname}</p>
            <p><strong>Time:</strong> {now}</p>
            <p style="color:green">This instance is healthy and serving traffic!</p>
        </body>
        </html>
        """
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(body.encode())

    def log_message(self, format, *args):
        pass

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 80), Handler)
    print("Server running on port 80...")
    server.serve_forever()
