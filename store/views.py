from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Book


class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('book_list')
        return redirect('login')


class RegisterView(View):
    def get(self, request):
        return render(request, 'store/register.html')

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return render(request, 'store/register.html')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Registration successful! Please log in.")
        return redirect('login')


class LoginView(View):
    def get(self, request):
        return render(request, 'store/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "You have successfully logged in!")
            return redirect('book_list')
        else:
            return render(request, 'store/login.html', {'error': 'Invalid credentials'})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')


class BookListView(LoginRequiredMixin, View):
    def get(self, request):
        query = request.GET.get('q')
        category = request.GET.get('category')

        books = Book.objects.all()

        if query:
            books = books.filter(title__icontains=query)
        if category and category != 'all':
            books = books.filter(category__iexact=category)

        categories = Book.objects.values_list('category', flat=True).distinct()
        paginator = Paginator(books, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'store/book_list.html', {
            'books': page_obj,
            'categories': categories,
            'page_obj': page_obj
        })


class BookDetailView(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        return render(request, 'store/book_detail.html', {'book': book})


class AddToCartView(LoginRequiredMixin, View):
    def get(self, request, book_id):
        cart = request.session.get('cart', {})
        if not isinstance(cart, dict):
            cart = {}

        book_id_str = str(book_id)
        if book_id_str in cart:
            cart[book_id_str] += 1
        else:
            cart[book_id_str] = 1

        request.session['cart'] = cart
        messages.success(request, "Book added to cart!")
        return redirect('cart')


class CartView(LoginRequiredMixin, View):
    def get(self, request):
        cart = request.session.get('cart', {})
        book_ids = cart.keys()
        books = Book.objects.filter(id__in=book_ids)

        cart_items = []
        total_price = 0

        for book in books:
            book_id_str = str(book.id)
            quantity = cart.get(book_id_str, 0)
            subtotal = book.price * quantity
            total_price += subtotal
            cart_items.append({
                'book': book,
                'quantity': quantity,
                'subtotal': subtotal
            })

        return render(request, 'store/cart.html', {
            'cart_items': cart_items,
            'total_price': total_price
        })


class UpdateCartView(LoginRequiredMixin, View):
    def post(self, request, book_id):
        quantity = int(request.POST.get('quantity', 1))
        cart = request.session.get('cart', {})

        if quantity > 0:
            cart[str(book_id)] = quantity
        else:
            cart.pop(str(book_id), None)

        request.session['cart'] = cart
        return redirect('cart')


class RemoveFromCartView(LoginRequiredMixin, View):
    def get(self, request, book_id):
        cart = request.session.get('cart', {})
        book_id_str = str(book_id)

        if book_id_str in cart:
            if cart[book_id_str] > 1:
                cart[book_id_str] -= 1
            else:
                cart.pop(book_id_str)

        request.session['cart'] = cart
        return redirect('cart')


class ClearCartView(LoginRequiredMixin, View):
    def get(self, request):
        request.session['cart'] = {}
        return redirect('cart')
