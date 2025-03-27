import requests

def test_file_upload(base_url):
    files = {'file': open('example.jpg', 'rb')}
    response = requests.post(f'{base_url}/upload', files=files)
    assert response.status_code == 200
    assert 'file' in response.json()
    files['file'].close()