#TODO: Reorganize the imports
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseForbidden
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
import googlemaps
from .forms import BookingForm, JoinForm
from .models import Booking
from car.models import Car
from datetime import datetime

#TODO: Move booking to another place maybe in the models
def get_cars():
	#TODO: maybe change the return in exception to empty list so we have a consisant return type
	"""
	This function return all available cars
	:return: Cars with diponility = True
	:rtype: list of Car objects

	:exception ObjectDoesNotExist: if there is no car available return None

	"""
	try:
		return Car.objects.filter(disponibility=True)
	except ObjectDoesNotExist:
		return None

def set_car_disponibility(id_car, state):
	"""
	This function set the car disponibility
	:param id_car: id of the car
	:param state: State of the car (True if the car is available False else)
	:return:
	"""
	try:
		car = Car.objects.get(id=id_car)
		car.disponibility = state
		car.save()
	except ObjectDoesNotExist:
		return None

def get_booking(id_booking):
	"""
	This function search retreive the booking with id_booking
	:param id_booking: id of the booking
	:return: Booking object if it exist else None
	"""
	try:
		return Booking.objects.get(id=id_booking)
	except ObjectDoesNotExist:
		return None


def get_bookings(user_request):
	#TODO: Change function name
	#TODO: Change return type to get a consistant return type
	"""
	Get all the booking to a related user
	:param user_request: user we want bookings
	:return: All the booking related to a user
	:rtype: list of Booking objects
	"""
	try:
		return Booking.objects.filter(user=user_request)
	except ObjectDoesNotExist:
		return None

def delete_booking(id_booking):
	#TODO: Move this function to the model
	"""
	LOGIC
	=====
		Get the booking
		set the car disponibility to True
		delete the booking
	:param id_booking:
	:return:
	"""
	try:
		inst = Booking.objects.get(id=id_booking)
		set_car_disponibility(inst.car.id, True)
		return inst.delete()
	except ObjectDoesNotExist:
		return None

# gmaps direction

def get_duration(start_address, dest_address):
	gmaps = googlemaps.Client(key='HARDCODED_KEY')
	now = datetime.now()
	try:
		directions_result = gmaps.directions(
			start_address,
			dest_address,
			mode="driving",
			departure_time=now)
		return directions_result[0]['legs'][0]['duration_in_traffic']['text']
	except googlemaps.exceptions.ApiError as inst:
		raise Http404(inst.args[0])

# Views functions

def home(request):
	data = get_bookings(request.user)
	return render(request,'booking/home.html', dict([("bookings", data)]))

def booking(request, bookingID):
	data = get_booking(bookingID)
	if data.user == request.user:
		return render(
			request,
			'booking/booking.html',
			dict([('booking', data)])
		)
	else:
		return HttpResponseForbidden()

def new(request):
	form = BookingForm(request.POST or None)
	if form.is_valid():
		booking = Booking()
		booking.user = request.user
		booking.reservation_date = datetime.now()
		booking.start_address = form.cleaned_data['start_address']
		booking.dest_address = form.cleaned_data['dest_address']
		booking.duration = get_duration(booking.start_address, booking.dest_address)
		booking.state = True

		if get_cars():
			booking.car = get_cars()[0]	#TODO: maybe use variable

			set_car_disponibility(get_cars()[0].id, False)
		booking.save()
		return redirect('/bookings/' + str(booking))

	return render(request, 'booking/new.html', locals())

def delete(request, bookingID):
	delete_booking(bookingID)
	data = get_bookings(request.user)

	return render(request,'booking/home.html', dict([("bookings", data)]))

def join(request):
	form = JoinForm(request.POST or None)
	if form.is_valid():
		userDjango = User.objects.create(
			username = form.cleaned_data['email'],
			last_name = form.cleaned_data['surname'],
			first_name = form.cleaned_data['firstname'],
			email = form.cleaned_data['email'])

		userDjango.set_password(request.POST['password'])
		userDjango.save()
		return redirect('/bookings/login')

	return render(request, 'booking/join.html', locals())