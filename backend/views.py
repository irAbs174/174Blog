from django.shortcuts import render

def index(request):
    content = {
        'title':'174 Blog',
        'description': 'simple blog with django and directus',
        'keywords':'linux and security',
        'team': '174 Team',
    }
    return render(request, 'index.html', content)