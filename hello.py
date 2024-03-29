from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn, socket 
import threading
import logging 
import sys


class Handler(BaseHTTPRequestHandler):
    hostname = socket.gethostname()

    logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d/%b/%Y %H:%M:%S')
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    def do_GET(self):
        self.logger.info(f"Request from: {self.client_address[0]}")
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        content = f"<html><body><h1>Hello World!</h1><p>{self.hostname}</p></body></html>"
        self.wfile.write(content.encode('utf-8'))


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    pass


def main():
    port = 8000

    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except:
            pass 

    if port < 1024 or port > 65535:
        port = 8000

    server = ThreadedHTTPServer(('', port), Handler)
    server.serve_forever()


if __name__ == '__main__':
    main()
