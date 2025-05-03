from django.contrib import admin
from . models import Profile, Blog, Tag, Review, Inbox

admin.site.register(Profile)
admin.site.register(Blog)
admin.site.register(Tag)
admin.site.register(Review)
admin.site.register(Inbox)