from django.shortcuts import render
import json
import requests
from rest_framework import viewsets 
from .models import Item
from .serializers import ItemSerializer

class ItemView(viewsets.ModelViewSet): 
	queryset = Item.objects.all()
	serializer_class = ItemSerializer

def home(request):
	return render(request, 'home.html', {})

# Create your views here.
