from django.db import models

# Create your models here.

class ContactMe(models.Model):
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    # Mobile = models.IntegerField(null=True)
    Email = models.CharField(max_length=50)
    Message = models.CharField(max_length=255)
    date_time = models.DateField(null=True)


class help_db(models.Model):
    first_name = models.CharField(max_length=50 , null=True)
    last_name = models.CharField(max_length=50 , null=True)
    e_mail = models.CharField(max_length=50 , null=True)
    phone_num = models.IntegerField(null=True)
    message_query = models.CharField(max_length=250 , null=True)
    resolve_query = models.BooleanField(default = False)

class review_db(models.Model):
    name = models.CharField(max_length=50 , null=True)
    message = models.CharField(max_length=250 , null=True)
    star_rating = models.IntegerField(null=True)
