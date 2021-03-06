#TODO: Integrate Address model to Booking
#TODO: Change name to english name

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


from car.models import Car


class BookingManager(models.Manager):
	"""Booking model manager
	"""

	def get_booking(self, id_booking):
		"""
		This function search retreive the booking with id_booking
		:param id_booking: id of the booking
		:return: Booking object if it exist else None
		"""
		try:
			return Booking.objects.get(id=id_booking)
		except ObjectDoesNotExist:
			return None

	def get_bookings_related_to_user(self, user_request):
		# TODO: Change function name
		# TODO: Change return type to get a consistant return type
		"""
		Get all the booking to a related user
		:param user_request: user we want bookings
		:return: All the booking related to a user
		:rtype: list of Booking objects
		"""
		try:
			return Booking.objects.filter(user=user_request.id)
		except ObjectDoesNotExist:
			return None

	def delete_booking(self, id_booking):
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
			Car.objects.set_car_disponibility(inst.car.id, True)
			return inst.delete()
		except ObjectDoesNotExist:
			return None

class Booking(models.Model):
	create_date = models.DateTimeField(auto_now_add=True, auto_now=False,
                                verbose_name="Date de creation")
	booking_date = models.DateTimeField(auto_now_add=False, auto_now=False, verbose_name="Date de réservation")
	car = models.OneToOneField(Car, related_name='car')
	user = models.ForeignKey(User, related_name='user')
	start_address = models.CharField(max_length=250, verbose_name="Adresse de départ")
	dest_address = models.CharField(max_length=250, verbose_name="Adresse de destination")
	state = models.BooleanField() # TODO: What is the use of this field
	duration = models.CharField(max_length=10)

	objects = BookingManager()

	def __str__(self):
		return str(self.id)
