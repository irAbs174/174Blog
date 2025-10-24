from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests

@csrf_exempt
def post_list(request):
    data = requests.get('https://strange-kare-ive7vog0s.liara.run/items/posts').json()['data']
    return JsonResponse({
        'success': True,
        'data':data
    })