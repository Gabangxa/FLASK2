from flask import Flask, render_template
import os
print(os.getenv('REPLIT_DB_URL'))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
  if 'REPLIT_DB_URL' in os.environ:
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)