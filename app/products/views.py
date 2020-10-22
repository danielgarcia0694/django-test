import json
from django.core import serializers
from django.core.exceptions import ValidationError
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from . import models


@csrf_exempt
def bulk_insert(request):
    data = json.loads(request.body)
    products = data.get('products', None)

    errors = 0
    products_report = []

    if products:
        for product in products:
            instance = models.Product(**product)
            try:
                instance.full_clean()
            except ValidationError as e:
                report = {
                    'product_id': product['id'],
                    'errors': e.messages
                }
                products_report.append(report)
                errors += 1
            else:
                instance.save()

        if errors:
            return JsonResponse({
                'status': 'ERROR',
                'products_report': products_report,
                'number_of_products_unable_to_parse': errors
            }, status=422)
        else:
            return JsonResponse({'status': 'OK'}, status=200)


def products(request):
    data = list(models.Product.objects.all().values())
    return JsonResponse({'products': data}, safe=False, status=200)