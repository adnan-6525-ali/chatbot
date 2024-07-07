from django.contrib import admin
from .models import review_db , help_db 

# Register your models here.

admin.site.register(review_db)
admin.site.register(help_db)