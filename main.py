from flask import Flask
import json

app = Flask(__name__)

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


if __name__ == "__main__":
    app.run()

