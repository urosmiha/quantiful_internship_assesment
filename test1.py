import urllib
import requests
import json

# Toke for accessing APIs on NOAA
token = 'xULOcOgFzeebYPPRaKDlQkdYKkHYJQrr'

main_url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/'
field = 'locations?'
api = 'locationcategoryid=ST&limit=52'

url = main_url + field + api
response = requests.get(url, headers={"token":token})

if response.status_code != 200:
	print('Oops something went wrong. Error: ', response.status_code)

else:
	json_response = response.json()
	# Get the state code for FLORIDA
	for state in json_response['results']:
		if state['name'] == 'Florida':
			#print(state['name'])
			#print(state['id'])		# Debugging
			state_id = state['id']

	
	
#print(state_id) #debug

url = main_url + 'data?' + 'datasetid=PRECIP_HLY&limit=1000&unit=metric&startdate=2000-07-24T14:00:00&enddate=2000-07-24T15:00:00&locationid=' + state_id

#print(url) #debug

response = requests.get(url, headers={"token":token})

if response.status_code != 200:
	print('Oops something went wrong. Error: ', response.status_code)
else:
	json_response = response.json()
	count = 0
	tmp = 0
	for reading in json_response['results']:
		#print(reading) #debug
		if reading['date'] == '2000-07-24T14:00:00':
			# value of 25399.75 means the reading is missing so we'll ignore it
			if reading['value'] < 25000:				
				count += 1
				tmp += reading['value']
				#print(reading['value'])
				
	
	# API datasheet specifies that unit is given in tenths of millimeters so multiply tmp by 0.1 to get mm
	avg = (tmp *0.1) / count
	print('Average precipitation: %.4f mm' % avg)

		