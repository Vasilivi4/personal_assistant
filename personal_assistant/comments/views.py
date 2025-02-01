from django.shortcuts import render, get_object_or_404, redirect
from comments.forms import CommentForm
from news.models import Post

def comment_list(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('comments:comment_list', post_id=post.id)
    else:
        form = CommentForm()

    return render(request, 'comments/comment_list.html', {
        'post': post,
        'comments': comments,
        'form': form,
    })