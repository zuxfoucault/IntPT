from django.contrib import admin

# Register your models here.

from ipts.models import Clinic, Choice 

class ChoiceInline(admin.StackedInline):
	model = Choice
	extra = 1

class ClinicAdmin(admin.ModelAdmin):
	inlines = [ChoiceInline]

admin.site.register(Clinic, ClinicAdmin)
