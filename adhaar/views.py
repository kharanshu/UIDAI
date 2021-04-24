from django.shortcuts import render, redirect
from adhaar.models import *

# Create your views here.

def homepage(request):
    all_person = Person.objects.all()
    all_adhaar = Adhar.objects.all()
    # print(all_books)
    return render(request,template_name='home.html',context={"person":all_person , "adhar":all_adhaar})

def save_person(request):
    p_name = request.POST.get("name")
    p_email = request.POST.get("email")
    p_mobile = request.POST.get("mobile")
    person_obj = Person(name=p_name, email=p_email, mobile=p_mobile)
    person_obj.save()
    return redirect('welcome')

def save_adhaar(request):
    a_sign = request.POST.get("signature")
    a_num = request.POST.get("person")
    adhar_obj = Adhar(signature=a_sign,adhar_no=a_num)
    adhar_obj.save()
    return redirect('welcome')
