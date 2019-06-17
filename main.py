from flask import Flask
import json

app = Flask(__name__)
APP_VERSION = "0.0.1"


@app.route("/")
def list_resources():
    return json.dumps({
        "pizzas": [
            "hawaian",
            "capriciosa",
            "margharitta",
            "salame",
            "diavolo"
        ]
    })

# To jest branch master

@app.route("/version_info")
def app_version():
    return str(APP_VERSION)

if __name__ == "__main__":
    app.run()

