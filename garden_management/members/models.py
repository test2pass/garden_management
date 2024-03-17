from django.db import models

# Create your models here.
#All models created here will be add to db.sqlite3 as a tables
class Member(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    e_mail = models.CharField(max_length = 255, null = True)
    joined_date = models.DateField(null = True)