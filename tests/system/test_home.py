"""
Test that based on flask test_client()
2 checks - response status code and response message
Use this command line to run test
python -m pip install -r requirements.txt
python -m pytest -v --tb=line
"""

import app
import json


def test_home():
    with app.micro_service.test_client() as ms:
        res = ms.get('/')
        assert res.status_code == 200
        assert json.loads(res.get_data()) == {'message': 'Hello, world!'}
