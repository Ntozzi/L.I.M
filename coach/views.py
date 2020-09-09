from django.shortcuts import render
from .models import Coach
# Create your views here.

def coaches(request):
    text = Coach.objects.all().order_by('-date')[:5]
    return render(request,'Coach/coach.html',{'text': text})

