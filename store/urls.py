from django.urls import path
from .views import (
    HomeView, RegisterView, LoginView, LogoutView,
    BookListView, BookDetailView,
    AddToCartView, CartView, UpdateCartView,
    RemoveFromCartView, ClearCartView
)
from adminpanel.views import AdminDashboardView  # Update this line


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('books/', BookListView.as_view(), name='book_list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),

    path('add-to-cart/<int:book_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/', CartView.as_view(), name='cart'),
    path('update-cart/<int:book_id>/', UpdateCartView.as_view(), name='update_cart'),
    path('remove-from-cart/<int:book_id>/', RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('clear-cart/', ClearCartView.as_view(), name='clear_cart'),
    path('', AdminDashboardView.as_view(), name='admin_dashboard'),
]
