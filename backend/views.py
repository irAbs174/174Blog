from django.shortcuts import render
import requests

def index(request):
    res = requests.get('https://strange-kare-ive7vog0s.liara.run/items/menu').json()['data']
    id_map = {item['id']: {**item, 'children': []} for item in res}
    menu = []
    for item in id_map.values():
        if item['parent']:
            parent = id_map.get(item['parent'])
            if parent:
                parent['children'].append(item)
        else:
            menu.append(item)
    content = {
        'title':'174 Blog',
        'description': 'simple blog with django and directus',
        'keywords':'linux and security',
        'team': '174 Team',
        'menu': menu,
        'logo': 'https://strange-kare-ive7vog0s.liara.run/assets/394e1968-f966-4df3-b462-c6581b423380.png',
    }
    return render(request, 'index.html', content)