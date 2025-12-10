#!/usr/bin/env python3
"""
SafeHer Demo Server - UI Only
Developer: Vivek P S
Email: viveksubhash4@gmail.com

This demo server only serves static UI files.
Purchase the full project for complete Django backend.
"""

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

class DemoHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(Path(__file__).parent / "templates"), **kwargs)
    
    def do_GET(self):
        print(f"\n{'='*50}")
        print("SafeHer Demo - UI Only Version")
        print("Developer: Vivek P S")
        print("Email: viveksubhash4@gmail.com")
        print(f"{'='*50}")
        
        if self.path == "/" or self.path == "/home/":
            self.path = "/loading.html"
        elif self.path.startswith("/api/") or self.path.startswith("/admin/"):
            self.send_response(403)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"""
            <html><body style="font-family: Arial; text-align: center; padding: 50px;">
            <h1 style="color: #e91e63;">Demo Version - Backend Disabled</h1>
            <p>This is a UI-only demo version.</p>
            <p><strong>Developer:</strong> Vivek P S</p>
            <p><strong>Email:</strong> viveksubhash4@gmail.com</p>
            <p>Purchase the full project to access backend functionality.</p>
            </body></html>
            """)
            return
        
        super().do_GET()

if __name__ == "__main__":
    PORT = 8000
    print(f"\n{'='*60}")
    print("SafeHer Demo Server - UI Only Version")
    print("Developer: Vivek P S")
    print("Email: viveksubhash4@gmail.com")
    print(f"\nStarting demo server on port {PORT}")
    print("This is a UI-only demo. Purchase full project for backend.")
    print(f"{'='*60}\n")
    
    with socketserver.TCPServer(("", PORT), DemoHandler) as httpd:
        print(f"Demo server running at http://localhost:{PORT}")
        webbrowser.open(f"http://localhost:{PORT}")
        httpd.serve_forever()