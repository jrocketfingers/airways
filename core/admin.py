from django.contrib import admin

from core import models

class Admin(admin.ModelAdmin):
    exclude = ('created_at', 'created_by', 'updated_at', 'updated_by',
               'deleted_at', 'deleted_by')

# Register your models here.
admin.site.register(models.Company, Admin)
admin.site.register(models.Flight, Admin)
admin.site.register(models.FlightUpdate, Admin)
