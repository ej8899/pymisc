import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        # Define your response data as a dictionary
        response_data = {
            'message': 'Hello, this is your API endpoint!',
            'status': 'success'
        }
        
        # Convert the response data to a JSON string
        response_json = json.dumps(response_data)
        
        # Write the JSON response to the client
        self.wfile.write(response_json.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=SimpleHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
