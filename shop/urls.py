from django.urls import path,include
#views a import panrom . yathk na same project la view aaga

from . import views

# orupattern create panrom, path set panrom,home nu views.home 
# nu kodukrom,name if we want give
# oru oru vaatiyumm nammma html file create panan aprm
# path a inga save pannumm

urlpatterns = [
    path('',views.home,name="home"),
    path('register/',views.register,name="register"),
    path('login/',views.login_page,name="login"),
    path('logout/',views.logout_page,name="logout"),
    path('cart/',views.cart_page,name="cart"),
    path('fav/',views.fav_page,name="fav"),
    path('favviewpage/',views.favviewpaage,name="favviewpage"),

    path('remove_fav/<str:fid>',views.remove_fav,name="remove_fav"),
    path('remove_cart/<str:cid>',views.remove_cart,name="remove_cart"),

    path('collections/',views.collections,name="collections"),
    path('collections/<str:name>',views.collectionsview,name="collections"),
    #yathk na andha product click panna athooda fulll details solrthuuu str:....
    path('collections/<str:cname>/<str:pname>',views.product_details,name="product_details"),
    path('addtocart/',views.add_to_cart,name="addtocart"),
    


]
