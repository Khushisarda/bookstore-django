from django.views import View
from django.shortcuts import render
from store.models import Book

class AdminDashboardView(View):
    def get(self, request):
        # Retrieve all books (you can customize this as needed)
        books = Book.objects.all()

        # Render the custom admin dashboard template
        return render(request, 'adminpanel/dashboard.html', {
            'books': books,
        })
