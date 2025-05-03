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
        
        


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    total_votes = models.IntegerField(default=0)
    percentage = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}'s blog"

    class Meta:
        ordering = ['-created']

    @property
    def validation(self):
        total_votes = self.review_set.all()
        up_votes = total_votes.filter(vote_type = 'up')
        total = total_votes.count()
        percentage = (up_votes.count()/total) * 100
        self.total_votes = total
        self.percentage = percentage
        self.save()

    @property
    def users_list(self):
        lst = self.review_set.all().values_list('writer__pk', flat=True)
        return lst


class Tag(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.blog} | {self.name}"




class Review(models.Model):
    choices = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote')
    )
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    vote_type = models.CharField(max_length=200, choices=choices)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.blog.title} = {self.writer.username} = {self.vote_type}"