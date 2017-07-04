#TODO: Integrate Address model to Booking

from django.db import models
from django.contrib.auth.models import User

from car.models import Car


class Address(models.Model):
	#TODO: make some research about the zipcode to check if its always an integer worldwide
	"""
	Address model

	Attributes
	==========
	street_number: its a charfield because of this particular case "32 bis"
	street_name: name of the street
	city: city of the address
	zippcode: zippcode of the address
	country: country of the address
	"""
	street_number = models.CharField(max_length=32, verbose_name="Street number")
	street_name = models.CharField(max_length=128, verbose_name="Street name")
	city = models.CharField(max_length=128, verbose_name="City")
	zipcode = models.CharField(max_length=32, verbose_name="Zipcode")

	def __str__(self):
		return

class Booking(models.Model):
	# TODO: Use of address model
    creation_date = models.DateTimeField(auto_now_add=True, auto_now=False,
                                	verbose_name="creation date")
    reservation_date = models.DateTimeField(auto_now_add=False, auto_now=False, verbose_name="reservation date")
    car = models.OneToOneField(Car, related_name='car')
    user = models.ForeignKey(User, related_name='user')
    start_address = models.CharField(max_length=250, verbose_name="Start address")
    dest_address = models.CharField(max_length=250, verbose_name="Destination address")
    state = models.BooleanField()
    duration = models.CharField(max_length=10)

    def __str__(self):
        return str(self.id)
