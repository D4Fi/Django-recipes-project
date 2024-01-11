from django.contrib import admin
from . import models


@admin.register(models.Cards)
class CardsAdmin(admin.ModelAdmin):
	pass
