"""
Countain utils file
For now only google map duration retrievment
split into module if this one is too big
"""

from datetime import datetime

import googlemaps


def get_duration(start_address, dest_address):
	#TODO: Move hardcoded key to settings
	#TODO: add error logging
	"""
	Change the rasise execption to unknown duration
	for exemple negative duration
	:param start_address: start address of the travel
	:param dest_address: destination addres of the travel
	:return: a string which is the duration
	"""
	try:
		gmaps = googlemaps.Client(key="HARDCODED KEY")
	except ValueError:
		return "Unknown duration"

	now = datetime.now()
	try:
		directions_result = gmaps.directions(
			start_address,
			dest_address,
			mode="driving",
			departure_time=now)
	except googlemaps.exceptions.ApiError as inst:
		duration = "Unknown duration"
		return duration
	try:
		duration = directions_result[0]['legs'][0]['duration_in_traffic']['text']
		return duration
	except Exception:
		return "Unknown duration"
