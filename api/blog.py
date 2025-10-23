from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def post_list(request):
    return JsonResponse({
        'success': True,
        'data': [
            {
                'title':'هک اخلاقی',
                'image':'/static/images/pngs/4.jpg',
                'category': 'علمی تخیلی',
                'writer':'عباس دمرچی',
                'url':'/'
                },
            {
                'title':'دوره سلامتی',
                'image':'/static/images/pngs/5.jpg',
                'category': 'علمی جنایی',
                'writer':'عباس دمرچی',
                'url':'/'
            }
        ]
    })