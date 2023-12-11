from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from home.models import Form
from home.models import Feedback
from home.models import Cod
def home(request):
    return render(request,"home.html")

def contact(request):
    return render(request,"contact.html")


def redirect(request):
    return render(request,"redirect.html")
 
def about(request):
    if request.method=='POST':
        feedback = request.POST['feedback']
       
        print(feedback)
        ins = Feedback(feedback=feedback)
        ins.save()
        
        print('The data has been written to the db')
        
    return render(request,"about.html")

def menu(request):
    return render(request,"menu.html")
    
def meat(request):
    return render(request,"meat.html")
def cake(request):
    return render(request,"cake.html")

def snacks(request):
    return render(request,"snacks.html")
   
def form(request):
    if request.method == "POST":
        email = request.POST['email']
        name = request.POST['name']
        phone = request.POST['phone']
        pincode = request.POST['pincode']
        
       
        print(email,name,phone,pincode)
        ins = Form(email=email,name=name,phone=phone,pincode=pincode)
        ins.save()
        
        print('The data has been written to the db')
        return HttpResponseRedirect("/redirect1/")
        
    return render(request, "form.html")

def redirect1(request):
    return render(request,"redirect1.html")
def payment(request):
    return render(request,"payment.html")

def cardpage(request):
    if request.method == "POST":
        cardnumber = request.POST['cardnumber']
        expirationDate = request.POST['expirationDate']
        cvv = request.POST['cvv']
        cardHolderName = request.POST['cardHolderName']
        
       
        print(cardnumber,expirationDate,cvv,cardHolderName)
        ins = Cod(cardnumber=cardnumber,expirationDate=expirationDate,cvv=cvv,cardHolderName=cardHolderName)
        ins.save()
        
        print('The data has been written to the db')
        return HttpResponseRedirect("/redirect/")
    return render(request,"cardpage.html")

# def cardpage(request):
#     return render(request,"cardpage.html")