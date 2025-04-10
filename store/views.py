from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Book
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator


def home(request):
    books = Book.objects.all()
    return render(request, 'store/home.html', {'books': books})




def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('book_list')
        else:
            return render(request, 'store/login.html', {'error': 'Invalid credentials'})
    return render(request, 'store/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
@login_required
def book_list(request):
    query = request.GET.get('q')
    category = request.GET.get('category')

    books = Book.objects.all()

    if query:
        books = books.filter(title__icontains=query)
    if category:
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


@login_required
def add_to_cart(request, book_id):
    cart = request.session.get('cart', [])
    cart.append(book_id)
    request.session['cart'] = cart
    return redirect('cart')

@login_required
def cart(request):
    cart = request.session.get('cart', [])
    books = Book.objects.filter(id__in=cart)
    return render(request, 'store/cart.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'store/book_detail.html', {'book': book})

# Create your views here.
