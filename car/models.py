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


class Car(models.Model):
	disponibility = models.BooleanField()
	objects = CarManager()

	def __str__(self):
		return str(self.id)