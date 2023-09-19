from flask import Flask

app = Flask(__name__)

@app.route("/")
def root():
    prefix_google = """ 
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-ELHCY793ER"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'G-ELHCY793ER');
    </script>
    """
    return prefix_google + "Hello World 🚀"
