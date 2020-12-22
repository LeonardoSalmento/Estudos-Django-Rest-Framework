from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    phone_number = models.CharField(max_length=15, null=False)
    contacts = models.ManyToManyField('self', related_name = 'my_contacts')
    #blocked_contacts = models.ManyToManyField('self', symmetrical=False, related_name = 'my_contacts_blocked', through='lock')
    user = models.OneToOneField(User, related_name="profile", on_delete = models.CASCADE)
    justification = models.CharField(max_length=400)
    profile_picture = models.ImageField(upload_to='profile_picture', null=True, blank = True)

    @property
    def email(self):
        return self.usuario.email


