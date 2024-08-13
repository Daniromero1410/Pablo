from django.http.response import JsonResponse
from django.shortcuts import render
from .models import Ingenieria
# Create your views here.
def index(request):
    return render(request,'index.html')

def list_ingenierias(_request):
    ingenierias=list(Ingenieria.objects.values())
    data={'Ingenieria':ingenierias}
    return JsonResponse(data)
