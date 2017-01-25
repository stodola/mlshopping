from django.shortcuts import render, redirect
from .forms import  ParagonForm
from .models import Paragon
import pytesseract

from .tasks import items_from_image

from PIL import Image, ImageFilter

def start_page(request):
    return render(request,'base.html')


def lista_paragonow(request):
    qs = Paragon.objects.filter(user1=request.user)[::-1]  
    context={'qs':qs}
    return render(request, 'receipt/paragon_list2.html', context)


def add_receipt(request):
    if request.method == 'POST':
        form =ParagonForm(request.POST, request.FILES)
        print(request.FILES['image'])
        if form.is_valid():
            new_rec =form.save(commit=False)
            new_rec.user1=request.user            
            new_rec.save()
            items_from_image.delay(new_rec.image.name)
            return redirect('paragony:lista_paragonow')
    else:
        form =ParagonForm()
    
    context = {'form':form}
    return render (request, 'receipt/paragon_form.html', context)



