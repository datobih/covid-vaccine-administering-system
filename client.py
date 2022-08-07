import requests
endpoint='https://covid-vaccine-system.herokuapp.com/dummy_page/'


response=requests.get(endpoint)

print(response)