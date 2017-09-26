from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_data__isnull=False).order_by('-published_data')
	return render(request, 'blog/post_list.html', {'posts':posts})