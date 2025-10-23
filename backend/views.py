from django.shortcuts import render

def index(request):
    content = {
        'title':'174 Blog',
        'meta': 'simple blog with django and directus'
    }
    return render(request, 'index.html', content)