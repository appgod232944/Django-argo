from django.shortcuts import render
from .models import Kar

def index(request):
    kars = Kar.objects.all()  # Fetch all Kar instances from DB
    return render(request, 'index.html', {'kar_objects': kars})
