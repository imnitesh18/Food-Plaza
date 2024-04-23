from django.contrib import admin
from django.urls import path
from foodapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Home
    path('', views.foodapp, name='home'), 
    path('home', views.foodapp, name='home'), 
            
    # Food
    path('addfoods', views.addfood, name='addfoods'),
    path('deletefood/<int:FoodId>', views.deletefood, name='deletefood'),
    path('getfood/<int:FoodId>', views.getfood, name='getfood'),
    path('editfood/<int:FoodId>', views.updatefood, name='editfood'),
    path('allfood', views.showfood, name='allfood'),
            
    # Customer
    path('addcustomer', views.addcust, name='addcustomer'),
    path('deletecustomer/<int:CustId>', views.deletecust, name='deletecustomer'),
    path('getcustomer', views.getcust, name='getcustomer'),
    path('editcustomer/<int:CustId>', views.updatecust, name='editcustomer'),
    path('allcustomer', views.showcust, name='allcustomer'),
    
    # Update Password
    path('updatepasswd', views.updatepasswd, name='updatepasswd'),
    path('updatepassword', views.changepass, name='updatepassword'),
    
    # Login
    path('login', views.login, name='login'),
    path('dologin', views.doLogin, name='dologin'),
    path('logout', views.doLogout, name='logout'),
	
    # Cart
    path('addtocart/<int:FoodId>', views.addcart, name='addtocart'),
    path('allcart', views.showcart, name='allcart'),
    path('deletecart/<int:CartId>', views.delcart, name='deletecart'),
    path('updateqnty/<str:s>', views.updateQNT, name='updateqnty'),
	
    # Order
    path('placeorder', views.placeorder, name='placeorder'),
    path('orders', views.getorder, name='orders'),
]

# Static and media files serving during development
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
