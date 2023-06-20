from django.shortcuts import render
from .models import Customer
from .form import Customersform
from django.contrib import messages


# Create your views here.
def homepage(request):
    return render(request,template_name='homepage.html')



def Customer_view(request):
    if request.method=='POST':
        Customers_form=Customersform(request.POST)
        if Customers_form.is_valid():
            Customers_form.save()
            messages.success(request,('your data is successful added'))
        else:
            messages.error(request,('your data is invalid try again'))
    Customers_form=Customersform() 
    return render(request=request,template_name='Customer_view.html',context={'Customers_form':Customers_form})

def Customer_list(request):
    Customers=Customer.objects.all()
    return render(request, "Customers_list.html", {'Customers':Customers})

def Phone_view(request):
    Phones=Phone.objects.all()
    return render(request=request,template_name="Phone_view.html",context={'Phones':Phones})



        
    





  