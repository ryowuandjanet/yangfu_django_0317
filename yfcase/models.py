from django.conf import settings
from django.db import models
from django.urls import reverse

class Case(models.Model):
	casenumber = models.CharField(u"案號",max_length=100)
	city = models.CharField(u"縣市",max_length=20)
	township = models.CharField(u"鄉鎮區",max_length=20)
	section = models.CharField(u"段",max_length=20)
	small_section = models.CharField(u"小段",max_length=20)
	other_address = models.CharField(u"地址",max_length=200)
	author = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		blank=True, 
		null=True,
	)

	def __str__(self):
		return self.casenumber

	def get_absolute_url(self):
		return reverse('case_detail', args=[str(self.id)])

class Land(models.Model):
	case = models.ForeignKey(Case, on_delete=models.CASCADE)
	landnumber = models.CharField(u"地號",max_length=100	,blank=True, null=True)
	landurl = models.CharField(u"謄本",max_length=100,blank=True,null=True)
	landarea = models.DecimalField(u"地坪(平方公尺)",max_digits=7, decimal_places=2,blank=True,null=True)
	landholdingpointperson = models.IntegerField(u"個人持分",default=0,blank=True,null=True)
	landholdingpointall = models.IntegerField(u"所有持分",default=0,blank=True,null=True)

	def __str__(self):
		return self.landnumber

