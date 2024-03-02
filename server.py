from http.server import HTTPServer, BaseHTTPRequestHandler
import pickle
from job import Job
import env


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

    def do_GET(self):
        self.send_response(200)
        self.basic_headers()
        self.end_headers()

        new_job = Job(0, 1, 3, 0, 1, 3)

        self.wfile.write(pickle.dumps(new_job))


if __name__ == "__main__":
    server_address = ("0.0.0.0", env.SERVER_PORT)
    print("Serving on {}:{}".format(*server_address))
    print("Press Ctrl-C to quit")

    try:
        HTTPServer(server_address, FractalServer).serve_forever()
    except KeyboardInterrupt:
        print("\nExiting...")
        exit(0)
