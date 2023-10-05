from google.oauth2 import service_account
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.oauth2 import service_account
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
)
import logging
from html import unescape
from flask import Flask, render_template, request
import requests

app = Flask(__name__, static_url_path='/static')

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

credentials = service_account.Credentials.from_service_account_file(
    'nodale-424af451d4b3.json', scopes=['https://www.googleapis.com/auth/analytics.readonly']
)


def sample_run_report():
    """Runs a simple report on a Google Analytics 4 property."""
    user_count = 0
    property_id = "407507302"
    client = BetaAnalyticsDataClient(credentials=credentials)

    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="city")],
        metrics=[Metric(name="activeUsers")],
        date_ranges=[DateRange(start_date="2023-03-31", end_date="today")],
    )
    response = client.run_report(request)

    for row in response.rows:
        user_count += int(row.metric_values[0].value)

    return user_count


@app.route("/")
def root():
    """Home page"""
    return render_template("index.html")


@app.route("/logger", methods=['GET', 'POST'])
def logger():
    """ Log messages and send requests to Google"""
    log_message = "This is a log message"
    response_message = "This is a test"
    user_count = sample_run_report()

    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'Request':
            log_message = request.form.get('Request')
            logging.info(log_message)
        elif action == 'Google':
            response = requests.get("https://www.google.com")
            if response.status_code == 200:
                response_message = response.cookies.get_dict()
            else:
                response_message = "Request to Google failed."
        elif action == 'ganalytics':
            response = unescape(requests.get(
                "https://analytics.google.com/analytics/web/?authuser=1#/p407507302/reports/intelligenthome?params=_u..nav%3Dmaui"))
            if response.status_code == 200:
                response_message = response.text
            else:
                response_message = "Request to Google Analytics failed "

    return render_template("logger.html", log_message=log_message, response_message=response_message, user_count=user_count)


if __name__ == "__main__":
    app.run(debug=True)
