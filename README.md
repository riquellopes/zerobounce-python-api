# zerobounce-python-api

[ZeroBounce](https://www.zerobounce.net "Zerobounce Homepage") Python API.
The response object allows an attribute-like style access.


```python
from zerobounce import ZeroBounceAPI

zba = ZeroBounceAPI('yourapikey____________')
print zba.get_credits()
resp1 = zba.validate('flowerjill@aol.com')
resp2 = zba.validatewithip('flowerjill@aol.com')

print resp1
{
  "address": "flowerjill@aol.com",
  "status": "Valid",
  "sub_status": "",
  "account": "flowerjill",
  "domain": "aol.com",
  "disposable": False,
  "toxic": False,
  "firstname": "Jill",
  "lastname": "Stein",
  "gender": "female",
  "location": None,
  "creationdate": None,
  "processedat": "2017-04-01 02:48:02.592"
}

print resp2
{
  "address": "flowerjill@aol.com",
  "status": "Valid",
  "sub_status": "",
  "account": "flowerjill",
  "domain": "aol.com",
  "disposable": False,
  "toxic": False,
  "firstname": "Jill",
  "lastname": "Stein",
  "gender": "female",
  "location": None,
  "country": "United States",
  "region": "Florida",
  "city": "West Palm Beach",
  "zipcode": "33401",
  "creationdate": None,
  "processedat": "2017-04-01 02:48:02.592"
}

print resp.firstname
Jill

print resp2.status
Valid


```
