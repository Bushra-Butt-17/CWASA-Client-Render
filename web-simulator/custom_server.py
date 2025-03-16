from http.server import SimpleHTTPRequestHandler, HTTPServer

class NoCacheRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add headers to prevent caching
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

if __name__ == '__main__':
    server_address = ('', 8000)  # Serve on all available interfaces, port 8000
    httpd = HTTPServer(server_address, NoCacheRequestHandler)
    print("Serving HTTP on port 8000 with no-cache headers...")
    httpd.serve_forever()