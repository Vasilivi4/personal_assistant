from django.shortcuts import render, get_object_or_404, redirect
from comments.forms import CommentForm
from news.models import Post

def comment_list(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()

    image_files = [
        "https://res.cloudinary.com/dxcgfa3e2/image/upload/v1737404075/images/ftopxylji1twl9o4kfmh.png",
        "https://res.cloudinary.com/dxcgfa3e2/image/upload/v1737404076/images/nwmmcd1xfsokpk1brhdl.png",
        "https://res.cloudinary.com/dxcgfa3e2/image/upload/v1737404076/images/udb11ue7ytxwccrxq6mm.png",
        "https://res.cloudinary.com/dxcgfa3e2/image/upload/v1737404077/images/k6ofawgnhty1mdsxusf7.png",
        "https://res.cloudinary.com/dxcgfa3e2/image/upload/v1737404078/images/orabb09asjwykxqftade.png",
    ]

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
        'image_files': image_files,
    })
