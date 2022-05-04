from django.shortcuts import render
from django.http import HttpResponse

postlist = [
    {
        'author': 'İlhan',
        'title': 'BP1',
        'content': 'FP CONTENT',
        'date_posted': '27.04.2022'
    },
    {
        'author': 'Abdullah',
        'title': 'BP2',
        'content': 'SP CONTENT',
        'date_posted': '29.04.2022'
    }
]

def home(request):
    context = {
        'posts': postlist,
        'title': 'Home'
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
