from django.shortcuts import render, redirect
from .models import Comment
from .forms import CommentForm

def index(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CommentForm()

    comments = Comment.objects.all().order_by('-created_at')
    return render(request, 'comments/index.html', {'form': form, 'comments': comments})
