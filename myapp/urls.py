from django.urls import path
from myapp import views

urlpatterns =[
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('main/',views.main,name='main'),
    path('cart_page/<int:id>',views.cart_page,name="cart_page"),
    path('view_cart/',views.view_cart,name="view_cart"),
    path('checkout/',views.checkout,name="checkout"),
    path('success/',views.success,name="success"),
]