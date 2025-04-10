from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),

]
