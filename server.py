#!/usr/bin/env python3
"""
CAD Viewer Server - Serves 3D CAD files (STL, OBJ, IGES)
Includes IGES to STL conversion support
"""

import sys
import os
import json
import webbrowser
import tempfile
from threading import Timer
from pathlib import Path
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

PORT = 8080

# Try to import IGES converter
try:
    from iges_reader import IGESConverter, check_pythonocc
    IGES_SUPPORT = check_pythonocc()
except ImportError:
    IGES_SUPPORT = False
    IGESConverter = None


class CADHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/cad_viewer.html'
        elif self.path == '/iges-status':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {'iges_support': IGES_SUPPORT}
            self.wfile.write(json.dumps(response).encode())
            return
        return super().do_GET()

    def do_POST(self):
        if self.path == '/convert-iges':
            if not IGES_SUPPORT:
                self.send_response(503)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                error = {'error': 'IGES support not available. Install pythonocc-core.'}
                self.wfile.write(json.dumps(error).encode())
                return

            content_length = int(self.headers.get('Content-Length', 0))
            if content_length == 0:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'No file data'}).encode())
                return

            # Read IGES file from request
            iges_data = self.rfile.read(content_length)

            try:
                converter = IGESConverter()

                # Create temporary STL file
                with tempfile.NamedTemporaryFile(suffix='.stl', delete=False) as tmp:
                    stl_path = tmp.name

                # Convert IGES to STL
                converter.convert_bytes(iges_data, stl_path)

                # Read STL file
                with open(stl_path, 'rb') as f:
                    stl_data = f.read()

                # Clean up
                os.unlink(stl_path)

                # Send STL file
                self.send_response(200)
                self.send_header('Content-type', 'application/octet-stream')
                self.send_header('Content-Length', len(stl_data))
                self.end_headers()
                self.wfile.write(stl_data)

            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                error = {'error': f'Conversion failed: {str(e)}'}
                self.wfile.write(json.dumps(error).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def end_headers(self):
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()

    def log_message(self, fmt, *args):
        pass

def open_browser():
    webbrowser.open(f"http://localhost:{PORT}/")

if __name__ == "__main__":
    print("\n  ╔════════════════════════════════════════════╗")
    print("  ║         CAD 3D Viewer is Running           ║")
    print("  ╠════════════════════════════════════════════╣")
    print(f"  ║  Open Chrome and go to:                    ║")
    print(f"  ║  http://localhost:{PORT}                        ║")
    print("  ║                                            ║")
    print("  ║  Supported: STL, OBJ files                 ║")
    print("  ║  Press Ctrl+C to stop                      ║")
    print("  ╚════════════════════════════════════════════╝\n")

    Timer(1.0, open_browser).start()

    server = HTTPServer(("", PORT), CADHandler)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n  Server stopped. Goodbye!")
        sys.exit(0)
