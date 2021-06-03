from django.shortcuts import render,redirect
from mobileapp.models import Brand
from mobileapp.forms import BrandModelForm
# Create your views here.
def create_brand(request):
    if request.method=="GET":
        form=BrandModelForm()
        context={}
        context["form"]=form
        return render(request,"createbrand.html",context)
    elif request.method=="POST":
        form=BrandModelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"index.html")

def update_brand(request,id):
    brand=Brand.objects.get(id=id)
    form=BrandModelForm(instance=brand)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=BrandModelForm(instance=brand,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("listbrands")
    return render(request,"updatebrand.html",context)

def list_all_brands(request):
    brands=Brand.objects.all()
    context={}
    context["brands"]=brands
    return render(request,"listallbrands.html",context)

def delete_brand(request,id):
    brand=Brand.objects.get(id=id)
    brand.delete()
    return redirect("listbrands")

def index(request):
    return render(request,"index.html")