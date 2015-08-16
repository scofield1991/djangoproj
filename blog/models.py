from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user=models.OneToOneField(User)

    birthday=models.DateField()
    phone_regex= RegexValidator(regex=r'^[0-9]{3}-? ?[0-9]{7}$' , message="Phone number must be entered in the format: '999-9999999'.")
    phone_number = models.CharField(validators=[phone_regex], max_length=11)
    image= models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username