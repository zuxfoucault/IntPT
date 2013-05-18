from django.db import models

# Create your models here.

class Clinic(models.Model):
	cname = models.CharField(max_length=200)

	def __str__(self):
		return self.cname

class Choice(models.Model):
	clinic = models.ForeignKey(Clinic)
	choice_text = models.CharField(max_length=200)
	chosen = models.NullBooleanField()

	def __str__(self):
		return self.choice_text
