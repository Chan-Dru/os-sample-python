from flask import Flask
import os
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World , %d , %d , %s"%(os.getppid(),os.getpid(),os.uname()[1])

if __name__ == "__main__":
    application.run()
