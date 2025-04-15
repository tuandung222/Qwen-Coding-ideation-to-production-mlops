# test_api.py - Đơn giản test API /predict
import requests

def test_predict():
    url = "http://localhost:8000/predict"
    data = {
        "question": "What is the output of print(1+1)?",
        "choices": ["1", "2", "3", "4"]
    }
    resp = requests.post(url, json=data)
    assert resp.status_code == 200
    assert resp.json()["answer"] in data["choices"]
