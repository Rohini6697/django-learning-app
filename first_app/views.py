from django.shortcuts import render,redirect
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
def testing(request):
    context = {
        'fruits' : ['apple','banana','cherry']
    }
    return render(request,'testing.html',context)
def add(request):
    return render(request,'add.html')
def addrecord(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    new_member = Member(firstname = fname,lastname = lname)
    new_member.save()
    return redirect('index')
def deleterecord(request,id):
    member = Member.objects.get(id=id)
    member.delete()
    return redirect('index')
# def update(request):
#     return render(request,'update.html')
def updaterecord(request,id):
    member = Member.objects.get(id=id)
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        
        member.firstname = fname
        member.lastname = lname
        
        member.save()
        return redirect('index')
    return render (request,'update.html',{'member':member})