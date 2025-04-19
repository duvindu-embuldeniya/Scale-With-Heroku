from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE) 
    f_name = models.CharField(max_length=200, blank=True, null=True)
    l_name = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='profile_model/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
    
    @property
    def img_url(self):
        try:
            return self.image.url

        except Exception as ex:
            return '/static/images/static_profile_model/default.png'