import logging
from flask import Flask, render_template

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@app.route("/")
def root():
    return render_template("index.html")
    

@app.route("/logger")
def logger():
    logging.info("This is a log message")
    log_message = "This is a log message"
    return render_template("logger.html", log_message=log_message)


if __name__ == "__main__":
    app.run(debug=True)
