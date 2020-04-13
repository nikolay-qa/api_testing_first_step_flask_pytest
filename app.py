"""
Creating flask server that response with a json
"""

from flask import Flask
from flask import jsonify

micro_service = Flask(__name__)


@micro_service.route('/')  # http://mysite.com/
def home():
    return jsonify({'message': 'Hello, world!'})


if __name__ == '__main__':
    micro_service.run()

