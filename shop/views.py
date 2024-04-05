import json
from django.http import JsonResponse
from django.shortcuts import redirect, render
from shop.form import CustomUserForm
from . models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.

#oru fun create panit requ anuprom 
# nxt return panrom,
# enna return panrom na shop kulladi erka index.html file.

#oru fun create pannit athooda name dha url la kodukanummm

def home(request):
    Products=Product.objects.filter(trending=1)
    return render(request,"shop/index.html",{"category":Category,"products":Products})

def favviewpaage(request):
    if request.user.is_authenticated:
        fav=Favourite.objects.filter(user=request.user)
        return render(request,"shop/fav.html",{"fav":fav})
    else:
        return redirect("/")
    
def remove_fav(request,fid):
    cartitem=Favourite.objects.get(id=fid)
    cartitem.delete()
    return  redirect("/favviewpage")  

   
def cart_page(request):
    if request.user.is_authenticated:
        cart=Cart.objects.filter(user=request.user)
        return render(request,"shop/cart.html",{"cart":cart})
    else:
        return redirect("/")
    
def remove_cart(request,cid):
    cartitem=Cart.objects.get(id=cid)
    cartitem.delete()
    return  redirect("/cart")                                                        


def fav_page(request):
    if request.headers.get('x-requested-with')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            product_pid=(data['pid'])
            product_status=Product.objects.get(id=product_pid)
            if product_status:
                if Favourite.objects.filter(User=request.user.id,product_id=product_pid):
                    return JsonResponse({'status':'Product Added to Favourite'},status=200)
                else:    
                    Favourite.objects.create(user=request.user,Product_id=product_pid) 
                    return JsonResponse({'status':'Product Added To Favourite'},status=200)

        else:
            return JsonResponse({'status':'Log in to Add Favourite'},status=200)
    else:
        return JsonResponse({'status':'Invalid Access'},status=200)
    


def add_to_cart(request):
    if request.headers.get('x-requested-with')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            product_qty=(data['product_qty'])
            product_pid=(data['pid'])
            #print(request.user.id)
            product_status=Product.objects.get(id=product_pid)
            if product_status:
                if Cart.objects.filter(user=request.user,Product_id=product_pid).exists():
                    return JsonResponse({'status':'Product Already in Cart'},status=200)
                else:
                    if product_status.quantity>=product_qty: 
                        Cart.objects.create(user=request.user,Product_id=product_pid,Product_qty=product_qty) 
                        return JsonResponse({'status':'Product Added to Cart'},status=200)
                    else:
                        return JsonResponse({'status':'Invalid Access'},status=200)
    

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged out Successfully")
    return redirect("/")
        
def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            User=authenticate(request,username=name,password=pwd)
            if User is not None:
                login(request,User)
                messages.success(request,"Logged in Successfully")
                return redirect("/")
            else:
                messages.error(request,"shop/login.html")
                return redirect("/login")
        return render(request,"shop/login.html")


def register(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Success You Can Login Now...!")
            return redirect('/login')
    return render(request,"shop/register.html",{"form":form})

def collections(request):
    category=Category.objects.filter(status=0)
    return render(request,"shop/collections.html",{"category":category})
 
def collectionsview(request,name):
    if(Category.objects.filter(name=name,status=0)):
        products=Product.objects.filter(Category__name=name)
        return render(request,"shop/products/index.html",{"products":products,"category_name":name})
    else:
        messages.warning(request,"No Such Category Found")
        return redirect ('collections')
    

def product_details(request,cname,pname):
   if(Category.objects.filter(name=cname,status=0)):
       if(Product.objects.filter(name=pname,status=0)):
           Products=Product.objects.filter(name=pname,status=0).first()
           return render(request,"shop/products/product_details.html",{"products":Products})
       else:
           messages.error(request,"No Such Category Found")
           return redirect('collections')
   else:
       messages.error(request,"No Such Category Found")
       return redirect('collections')
        
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'shop/cart.html', {'cart': cart_items})
