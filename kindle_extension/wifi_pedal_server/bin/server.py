import subprocess
from http.server import *

class KindlePageHandler(BaseHTTPRequestHandler):
    def _forward(self):
        subprocess.run("cat /mnt/us/extensions/wifi_pedal_server/bin/f.txt > /dev/input/event1", shell=True)
    def _backward(self):
        subprocess.run("cat /mnt/us/extensions/wifi_pedal_server/bin/b.txt > /dev/input/event1", shell=True)
    def _wake_up(self):
        subprocess.run("powerd_test -i", shell=True)

    def handle_backward(self):
        self._backward()
        self._wake_up()
        return 1
    def handle_forward(self):
        self._forward()
        self._wake_up()
        return 1

    def do_GET(self):
        if self.path == "/forward":
            ret = self.handle_forward()
        if self.path == "/backward":
            ret = self.handle_backward()

        if ret:
            self.send_response(200)
        else:
            self.send_response(500)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        if ret:
            res = "<html>OK</html>"
        else:
            res = "<html>FAIL</html>"
        self.wfile.write(res.encode())

def run(server_class=HTTPServer, handler_class=KindlePageHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run()
