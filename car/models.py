from django.db import models
from django.core.exceptions import ObjectDoesNotExist


# Create your models here.

class CarManager(models.Manager):
	"""Custome car manager
	"""

	def get_available_cars(self):
		"""
        This function return all available cars
        :return: Cars with diponility = True
        :rtype: list of Car objects

        :exception ObjectDoesNotExist: if there is no car available return None

        """
		try:
			return Car.objects.filter(disponibility=True)
		except ObjectDoesNotExist:
			return []

	def set_car_disponibility(self, id_car, state):
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


class Car(models.Model):
	disponibility = models.BooleanField()
	objects = CarManager()

	def __str__(self):
		return str(self.id)