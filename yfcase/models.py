from django.conf import settings
from django.db import models
from django.urls import reverse

class Case(models.Model):
	casenumber = models.CharField(max_length=255)
	city = models.CharField(max_length=255)
	township = models.CharField(max_length=255)
	section = models.CharField(max_length=255)
	small_section = models.CharField(max_length=255)
	author = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
	)

	def __str__(self):
		return self.casenumber

	def get_absolute_url(self):
		return reverse('case_detail', args=[str(self.id)])

