from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseForbidden
from django.contrib.auth.models import User

from .forms import BookingForm, JoinForm
from .models import Booking
from car.models import Car
from .utils import get_duration

from datetime import datetime

def home(request):
	data = Booking.objects.get_bookings_related_to_user(request.user)
	return render(request,'booking/home.html', dict([("bookings", data)]))

def booking(request, bookingID):
	data = Booking.objects.get_booking(bookingID)
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

		available_car = Car.objects.get_available_cars()
		if available_car:
			booking.car = available_car[0]

			Car.objects.set_car_disponibility(booking.car.id, False)
		booking.save()
		return redirect('/bookings/' + str(booking)) #TODO: reverse function

	return render(request, 'booking/new.html', locals())

def delete(request, bookingID):
	Booking.objects.delete_booking(bookingID)
	data = Booking.objects.get_bookings_related_to_user(request.user)

	return render(request,'booking/home.html', dict([("bookings", data)]))

def join(request):
	form = JoinForm(request.POST or None)
	if form.is_valid():
		userDjango = User.objects.create(
			username = form.cleaned_data.get('email', ''),
			last_name = form.cleaned_data.get('surname', ''),
			first_name = form.cleaned_data.get('firstname', ''),
			email = form.cleaned_data.get('email', ''))

		userDjango.set_password(request.POST['password'])
		userDjango.save()
		return redirect('/bookings/login')

	return render(request, 'booking/join.html', locals())
