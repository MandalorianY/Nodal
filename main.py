import logging
from flask import Flask, render_template, request
import requests
app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
from html import unescape


@app.route("/")
def root():
    return render_template("index.html")
    

@app.route("/logger", methods=['GET', 'POST'])
def logger():
    logging.info("This is a log message")
    log_message="This a log message"
    response_message = "This is a test"
    
    if request.method == 'POST' and 'Request' in request.form:
        log_message = request.form.get('Request')
        logging.info(log_message)
        return render_template("logger.html", log_message=log_message)
    
    if request.method == 'POST' and request.form.get('action') == 'Google':
            response = requests.get("https://www.google.com")  
            if response.status_code == 200:
                response_message = response.cookies.get_dict()
            else:
                response_message = "Request to Google failed."
            return render_template("logger.html", log_message=log_message,response_message=response_message)
        
    if request.method == 'POST' and request.form.get('action') == 'ganalytics':
            print("HHH")
            response = unescape(requests.get("https://analytics.google.com/analytics/web/?authuser=1#/p407507302/reports/intelligenthome?params=_u..nav%3Dmaui")) 
            if response.status_code == 200:
                response_message = response.text
            else:
                response_message = "Request to Google failed."
            return render_template("logger.html", log_message=log_message,response_message=response_message)

    return render_template("logger.html", log_message=log_message,response_message=response_message)


if __name__ == "__main__":
    app.run(debug=True)
