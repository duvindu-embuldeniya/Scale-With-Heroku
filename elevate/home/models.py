from django.db import models
from django.contrib.auth.models import User

class Thought(models.Model):
    author = models.ForeignKey(User, on_delete=models.ForeignKey)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} | {self.author.username}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media_profile_model', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
    
    @property
    def imgUrl(self):
        try:
            return f"{self.image.url}"
        except Exception as ex:
            return f"/static/images/static_profile_model/default.png"
