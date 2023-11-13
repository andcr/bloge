from django.shortcuts import render
from .models import Post
from django.forms import Form


def create_post(request):
    if request.method == 'POST':
        form = Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = Form()

    return render(request, 'myapp/create_post.html', {'form': form})
def index(request):
    posts = Post.objects.all()
    return render(request, 'myapp/index.html', {'posts': posts})