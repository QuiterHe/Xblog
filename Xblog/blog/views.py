# coding=utf-8
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from haystack.forms import SearchForm

# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_data__isnull=False).order_by('-published_data')
	return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post':post})

@login_required
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			# TODO
			post.author = 1
			post.save()
			return redirect('blog.views.post_detail', pk=post.pk)

	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form':form})

@login_required
def post_edit(request, pk):
	# pass
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			# TODO
			post.author = 1
			post.save()
			return redirect('blog.views.post_detail', pk=post.pk)

	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form':form})

@login_required
def post_drafts_list(request):
	posts = Post.objects.filter(published_data__isnull=True).order_by('-published_data')
	return render(request, 'blog/post_draft_list.html', {'posts':posts})

@login_required
def post_publish(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.publish()
	return redirect('blog.views.post_detail', pk=pk)

def full_search(request):
	keywords = request.GET['q']
	sform = SearchForm(request.GET)
	posts = sform.search()
	return render(request, 'blog/post_search_list.html',{'posts': posts, 'list_header': '关键字 \'{}\' 搜索结果'.format(keywords)})

































