import argparse
import http.server
import socketserver

path = ""

class FileHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def do_GET(self):
        with open(path, 'rb') as file:
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(file.read())

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str)
    parser.add_argument('port', type=int)
    args = parser.parse_args()

    global path
    path = args.path

    with socketserver.TCPServer(('', args.port), FileHandler) as httpd:
        print(f'Serving {args.path} at http://localhost:{args.port}')
        httpd.serve_forever()

if __name__ == '__main__':
    main()