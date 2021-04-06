from django.contrib import admin
from .models import User, Location, Activity, HourCode

admin.site.register(User)
admin.site.register(Location)
admin.site.register(Activity)
admin.site.register(HourCode)

# Register your models here.
