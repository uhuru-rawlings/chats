from django.db import models
from authentication.models import Registration
# Create your models here.

# contacts
class Contacts(models.Model):
    user = models.ForeignKey(Registration, on_delete=models.CASCADE)
    contactname = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    date_added = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'Contacts'

    def __str__(self):
        return self.contactname
# messages

class Messages(models.Model):
    sender = models.ForeignKey(Registration, on_delete=models.CASCADE)
    receiver = models.ForeignKey(Contacts, on_delete=models.CASCADE)
    message = models.TextField(max_length=99999)
    time_sent = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Messages'

    def __str__(self):
        return self.time_sent
