from django.contrib import admin
from .models import User

#Customizes the admin site
admin.site.site_title = "EMS Admin Portal"


#Register the custom User model in the Django admin panel
admin.site.register(User)


