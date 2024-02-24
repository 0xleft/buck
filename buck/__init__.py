import argparse
import http.server
import socketserver

input = ""

class FileHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def do_GET(self):
        with open(input, 'rb') as file:
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(file.read())

class TextHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(input.encode())

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=str, help='Input file or text')
    parser.add_argument('mode', type=str, choices=['file', 'text'])
    parser.add_argument('--port', type=int, default=8000)
    args = parser.parse_args()

    # haky
    global input
    input = args.input

    if args.mode == 'file':
        handler = FileHandler
        try:
            with open(args.input, 'rb') as file:
                pass
        except FileNotFoundError:
            print(f'File {args.input} not found')
            return
    else:
        handler = TextHandler

    server = socketserver.TCPServer(('', args.port), handler)
    server.allow_reuse_address = True

    print(f'Serving {args.mode} on http://localhost:{args.port}')
    server.serve_forever()

if __name__ == '__main__':
    main()