import subprocess
import webbrowser

subprocess.Popen(['python', '-m', 'http.server'])

webbrowser.open('http://localhost:8000/index.html')