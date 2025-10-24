from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests

@csrf_exempt
def menu(request):
    res = requests.get('https://strange-kare-ive7vog0s.liara.run/items/menu').json()['data']
    id_map = {item['id']: {**item, 'children': []} for item in res}
    tree = []
    for item in id_map.values():
        if item['parent']:
            parent = id_map.get(item['parent'])
            if parent:
                parent['children'].append(item)
        else:
            tree.append(item)
            
    return JsonResponse({
        'success': True,
        'data':tree
    })