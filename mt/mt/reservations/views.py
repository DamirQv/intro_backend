from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Reservation
from django.contrib.auth.models import User
from tables.models import Table

@csrf_exempt
def create_reservation(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user = User.objects.get(id=data["user_id"])
        table = Table.objects.get(id=data["table_id"])
        
        if Reservation.objects.filter(user=user, data=data["date"]).exists():
            return JsonResponse({"error": "User already has a reservation for this date"}, status=400)
        
        if Reservation.objects.filter(table=table, data=data["date"]).exists():
            return JsonResponse({"error": "Table already has a reservation for this date"}, status=400)
        
        reservation = Reservation.objects.create(user=user, table=table, date=data["date"], status="pending")
        return JsonResponse({"id": reservation.id, "user_id": reservation.user.id, "table_id": reservation.table.id, "date": reservation.date, "status": reservation.status})
    
def get_reservations(request, id):
    try:
        reservation = Reservation.objects.get(id=id)
        return JsonResponse({"id": reservation.id, "user_id": reservation.user.id, "table_id": reservation.table.id, "date": reservation.date, "status": reservation.status})
    except Reservation.DoesNotExist:
        return JsonResponse({"error": "Reservation not found"}, status=404)
