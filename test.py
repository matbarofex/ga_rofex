import main
from flask import Flask, request

"""
Testing Locally

Use JSON samples in test_jsons folder

Run with the following command:
curl -H "Content-Type: application/json" -d @test_1.json localhost:8000
"""

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    return main.agent_fulfillment_handler(request)

app.run('127.0.0.1', 8000, debug=True)
