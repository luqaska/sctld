from flask import Flask
  
app = Flask(__name__)
  
@app.route("/")
def index():
  return "<h1>Welcome to Geeks for Geeks</h1>"

if __name__ == "__main__":
  app.run(port="80")
