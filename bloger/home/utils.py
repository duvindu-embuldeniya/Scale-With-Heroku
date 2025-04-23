from . models import Blog, Tag
from django.db.models import Q

def searchBlog(request):
    query = request.GET.get('query') if request.GET.get('query') else ''

    tags = Tag.objects.filter(
        name__icontains = query
    )

    blogs = Blog.objects.distinct().filter(
        Q(title__icontains = query) |
        Q(tag__in = tags)
    )

    return blogs, query