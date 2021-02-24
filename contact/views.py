from django.shortcuts import render

from .forms import ContactBusinessForm
from .models import ContactBusiness
def business_main(request):
    sent= False
    if request.method =='POST':
        business_form= ContactBusinessForm(request.POST)
        
        if business_form.is_valid():
            new_form= business_form.save(commit= False)
            new_form.save()
            sent= True
            return render(request, 'contact.html', {'sent':sent})
    else:
        business_form= ContactBusinessForm()
            
        
    return render(request, 'contact.html', {'business_form':business_form,'sent':sent})


def home(request):
    return render(request, 'index.html')