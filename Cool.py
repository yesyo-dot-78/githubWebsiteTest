from http.server import HTTPServer, SimpleHTTPRequestHandler
import webbrowser

port = 470
server_adress = ("", port)
httpd = HTTPServer(server_adress, SimpleHTTPRequestHandler)
webbrowser.get().open_new_tab("http://localhost:{port}")
httpd.serve_forever()
