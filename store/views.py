from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Book
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from .forms import RegistrationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = RegistrationForm()
    
    return render(request, 'store/register.html', {'form': form})

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
    cart = request.session.get('cart')

    # 🛠️ Fix: If cart is not a dictionary, reset it
    if not isinstance(cart, dict):
        cart = {}

    book_id_str = str(book_id)

    if book_id_str in cart:
        cart[book_id_str] += 1
    else:
        cart[book_id_str] = 1

    request.session['cart'] = cart
    return redirect('cart')



@login_required
def cart(request):
    cart = request.session.get('cart', {})
    book_ids = cart.keys()
    books = Book.objects.filter(id__in=book_ids)

    cart_items = []
    total_price = 0

    for book in books:
        quantity = cart[str(book.id)]
        subtotal = book.price * quantity
        total_price += subtotal
        cart_items.append({
            'book': book,
            'quantity': quantity,
            'subtotal': subtotal
        })

    return render(request, 'store/cart.html', {'cart_items': cart_items, 'total_price': total_price})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'store/book_detail.html', {'book': book})

# Create your views here.
