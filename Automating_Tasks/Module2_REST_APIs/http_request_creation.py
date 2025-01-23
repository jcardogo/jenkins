import requests
"""
response = requests.get('https://www.google.com')
print(response.text[:300])
"""

"""
response = requests.get('https://www.google.com', stream=True)
#print(response.raw.read()[:100])
#response.request.headers['Accept-Encoding']
#'gzip, deflate'
response.ok
response.status_code
"""

response = requests.get(url)
if not response.ok:
    raise Exception("Get failed with status code {}".format(response.status_code))

response = requests.get(url)
response.raise_for_status()

