from django.shortcuts import render,redirect
from .models import Userdata,Product,Cart,Checkoutinfo
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request,method=['GET','POST']):
    if request.method=='POST':
        email=request.POST.get('email')
        password1=request.POST.get('password1')

        users = Userdata.objects.filter(email=email,password=password1)
        if users.exists():
            request.session['email']=email
            return redirect('/main/')
    return render(request,'login.html')

def main(request):
    email=request.session['email']
    product=Product.objects.all()
    return render(request,'main.html',{'product':product,'email':email})

def signup(request,method=['GET','POST']):
    if request.method == 'POST':
        username = request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1') 
        password2=request.POST.get('password2')
        print(password1,password2)

        user=Userdata.objects.filter(email=email)

        if user.exists():
            messages.info(request,'User is already exits')
        elif password1 != password2 :
            messages.info(request,'Passwords does not match')
        else:
            Userdata.objects.create(username=username,email=email,password=password1)
            return render(request,'login.html')
       # print(email,password1,password2)
    return render(request,'signup.html')

def cart_page(request,id):
    email=request.session['email']
    user=Userdata.objects.get(email=email)
    product=Product.objects.get(id=id)
    cart_item,created = Cart.objects.get_or_create(user=user,product_item=product)
    
    if not created:
        cart_item.quantity+=1
        cart_item.save()
        return redirect("/view_cart/")

def view_cart(request):
    email=request.session['email']
    user=Userdata.objects.get(email=email)
    cart_item=Cart.objects.filter(user=user)
    total_sum=sum(i.product_item.dcost * i.quantity for i in cart_item)
    return render(request,'cart.html',{'cart_items':cart_item,'total_sum':total_sum})

def checkout(request):
    email=request.session['email']
    amount=request.GET['amount']
    
    return render(request,'checkout.html',{'amount':amount,'email':email})

def success(request):
    if request.method=="POST":
        email=request.POST.get('email')
        address=request.POST.get('address')
        country=request.POST.get('country')
        state=request.POST.get('state')
        zip=request.POST.get('zip')
        payment=request.POST.get('payment')
        
        Checkoutinfo.objects.create(email=email,address=address,country=country,state=state,zip=zip,payment=payment)
    
    return render(request,'success.html')