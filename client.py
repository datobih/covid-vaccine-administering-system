import requests
endpoint='https://covid-vaccine-system.herokuapp.com/patient/add-patient/'


credentials={'first_name':'Bola',
'last_name':'Tayo',
'gender':'Male',
'age':'17',
'genotype':'AA',
'blood_group':'O',
'phone_number':'08134343454'}


response=requests.post(endpoint,data=credentials)

print(response)