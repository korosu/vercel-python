from http.server import BaseHTTPRequestHandler
from urllib import parse

class handler(BaseHTTPRequestHandler):

	def do_GET(self):
		s = self.path
		dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
		self.send_response(200)
		self.send_header('Content-type','text/plain')
		self.end_headers()

		if "name" in dic:
			message = "Hello, " + dic["name"] + "!"
		else:
			message = "https://cdn.loom.com/sessions/transcoded/a55ca08c41fa417a8fd42a5a8496f8f8.mp4?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9jZG4ubG9vbS5jb20vc2Vzc2lvbnMvdHJhbnNjb2RlZC9hNTVjYTA4YzQxZmE0MTdhOGZkNDJhNWE4NDk2ZjhmOC5tcDQiLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE2NjA1ODQxNjN9fX1dfQ__&Key-Pair-Id=APKAJQIC5BGSW7XXK7FQ&Signature=NDuPieLQ8d2TuLZx3iDeN1hmlk3-js3yHG1zdAuwxptDmVjeX%7EgeGEj2r8nqk9UQcBYVETaQui222lanMzhRVrtTlHuldDyGkAfSdqy9DTcYrO7OKc6eOQPKvhC2EGjRKHIaX7R4pZOQ0fZGS5HgkTHZWO8IQTOpjqXp8zhBI-8v3qiQ6NVS6qc15JVufaAd73qo6hu-nSL3XqjWfTt5pVO5ZHr6tHqwDCSjRHXK5gihdskM1OY7BLtPGIS7BskhtZHMx6rZka3cFkHdgdYSS0rr3-XVOUkcUqyrlkBruZDcTay6gs%7EIew8JApmvWrnQymyWNrwtjKbxzT3PnvCv%7Ew__"

		self.wfile.write(message.encode())
		return
