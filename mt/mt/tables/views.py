from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Table

@csrf_exempt
def create_table(request):
    if request.method == "POST":
        data = json.loads(request.body)
        table = Table.objects.create(number=data["number"], seats=data["seats"])
        return JsonResponse({"id": table.id, "number": table.number, "seats": table.seats})
    
def get_tables(request):
    tables = list(Table.objects.values("id", "number", "seats", "is_available"))
    return JsonResponse(tables, safe=False)