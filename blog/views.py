from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        "title": "Post 1",
        "content": "Content of post 1",
        "author": "Prashant Singh",
        "date_posted": "August, 26",
    },
    {
        "title": "Post 2",
        "content": "Content of post 2",
        "author": "Nishita Singh",
        "date_posted": "May, 26",
    },
    {
        "title": "Post 3",
        "content": "Content of post 3",
        "author": "S B Singh",
        "date_posted": "January, 26",
    },
]


def home(request):
    context = {"posts": posts}
    return render(request, "blog/home.html", context)


def about(request):
    context = {"title": "About"}
    return render(request, "blog/about.html", context)
