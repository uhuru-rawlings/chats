from pyexpat import model
from django.db import models

# Create your models here.
class Registration(models.Model):
    username = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    userimage = models.ImageField(upload_to='users/')
    password = models.CharField(max_length=366)
    is_active = models.BooleanField(default=True)
    logedin = models.BooleanField(default=False)
    last_login = models.DateTimeField()
    date_created = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Registration'

    def __str__(self):
        return self.username