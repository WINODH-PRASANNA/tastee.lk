from django.urls import path
from . import views

urlpatterns= [
   path('', views.home, name="home"),
   path('register', views.register, name="register"),
   path('login', views.login_page, name="login"),
   path('logout', views.logout_page, name="logout"),
   path('cart', views.cart_page, name="cart"),
   path('favviewpage',views.favviewpage,name="favviewpage"),
   path('remove_fav/<str:fid>',views.remove_fav,name="remove_fav"),
   path('remove_cart/<str:cid>',views.remove_cart,name="remove_cart"),
   path('fav',views.fav_page,name="fav"),
   path('collection', views.collection, name="collection"),
   path('collection/<str:name>', views.collectionview, name="collection"),
   path('collection/<str:cname>/<str:pname>', views.product_details, name="product_details"),
   path('addtocart', views.add_to_cart, name="addtocart"),
   path('about', views.about, name="about"),
   path('contact', views.contact, name="contact"),
]
