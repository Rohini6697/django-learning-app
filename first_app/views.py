from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

# Create your views here.
def index(request):
    mymembers = Member.objects.all().values()
    return render(request,'index.html',{'person':mymembers})
    
def details(request,id):
    mymembers_details = Member.objects.get(id=id)
    return render(request,'details.html',{'person':mymembers_details})

def main(request):
    return render(request,'main.html')