from django.shortcuts import render, redirect
from .models import Member
from django.http import HttpResponse, Http404

# Create your views here.
def index(request):
    mem=Member.objects.all()
    return render(request, 'index.html', {'mem': mem})

def add(request):
    return render(request, 'add.html')

def addrec(request):
    x=request.POST['first']
    y=request.POST['last']
    z=request.POST['department']
    mem=Member(firstname=x, lastname=y, department=z)
    mem.save()
    return redirect('/')

def delete(request, id):
    mem=Member.objects.get(id=id)
    mem.delete()
    return redirect('/')

def update(request, id):
    mem=Member.objects.get(id=id)
    return render(request, 'update.html', {'mem': mem})

def uprec(request, id):
    x=request.POST['first']
    y=request.POST['last']
    z=request.POST['department']
    mem=Member.objects.get(id=id)
    mem.firstname=x
    mem.lastname=y
    mem.department=z 
    mem.save()
    return redirect('/')
