from http.server import HTTPServer, BaseHTTPRequestHandler


class FractalServer(BaseHTTPRequestHandler):
    def basic_headers(self):
        self.send_header("Connection", "close")

    def send_file(self, file, content_type="text/html"):
        f = open(file, "rb")
        content = f.read()
        f.close()

        self.send_response(200)
        self.basic_headers()
        self.send_header("Content-Length", len(content))
        self.send_header("Content-Type", content_type)
        self.end_headers()
        self.wfile.write(content)

    def redirect(self, page):
        self.send_response(301)
        self.send_header("Location", page)
        self.basic_headers()
        self.end_headers()

    def do_GET(self):
        if self.path == "/":
            self.redirect("/index.html")


if __name__ == "__main__":
    server_address = ("localhost", 8000)
    print("Serving on {}:{}".format(*server_address))
    print("Press Ctrl-C to quit")
    try:
        HTTPServer(server_address, CS2610Assn1).serve_forever()
    except KeyboardInterrupt:
        print("\nExiting...")
        exit(0)
