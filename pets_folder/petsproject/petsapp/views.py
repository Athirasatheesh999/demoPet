from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import Pets
from.forms import PetsForm
# Create your views here.
def index(request):
    pets=Pets.objects.all()
    context={
        'pets_list':pets
    }
    return render(request,'index.html',context)
def detail(request,pets_id):
    pets=Pets.objects.get(id=pets_id)
    return render(request,"detail.html",{'pets':pets})
def add_pets(request):
    if_request.method=='POST'
    name=request.POST.get('name')
    desc=request.POST.get('desc')
    price=request.POST.get('price')
    img=request.FILES['img']
    pets=Pets(name=name,desc=desc,price=price,img=img)
    pets.save()
    return render(request,'add.html')
def update(request,id):
    pets=Pets.objects.get(id=id)
    form=PetsForm(request.POST or None,request.FILES,instance=pets)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'pets':pets})
def delete(request,id):
    if request.method=='POST':
        pets=Pets.objects.get(id=id)
        pets.delete()
        return redirect('/')
    return render(request,'delete.html')