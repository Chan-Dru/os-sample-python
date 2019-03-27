from flask import Flask
import os
application = Flask(__name__)

@application.route("/")
def hello():
    return "%s"%(os.uname()[1])

if __name__ == "__main__":
    application.run()
