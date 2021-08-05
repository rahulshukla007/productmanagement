from django.shortcuts import render, redirect
from . models import Item
import os

def HomePage(request):
    products = Item.objects.all()
    context = {'products':products}
    print(context)
    return render(request, 'home.html', context)


#for adding a product
def addProduct(request):
    if request.method == "POST":
        prod = Item()
        prod.product_name = request.POST.get('pname')
        prod.description = request.POST.get('description')
        prod.category = request.POST.get('category')
        prod.image = request.FILES['image']
        prod.save()
        return redirect('/')
    else:
         return render(request, 'add.html')



#for edit a product
def editProduct(request, pk):
    prod = Item.objects.get(id=pk)

    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(prod.image)>0:
                os.remove(prod.image.path)
            prod.image = request.FILES['image']
        prod.product_name = request.POST.get('pname')
        prod.description = request.POST.get('description')
        prod.category = request.POST.get('category')
        prod.save()
        return redirect('/')
    context = {'prod':prod}
    return render(request, 'edit.html', context)


#for delete a product
def delProduct(request, pk):
    prod = Item.objects.filter(id=pk)
    prod.delete()
    return redirect('/')
    return render(request, 'add.html')

