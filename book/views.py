from django.shortcuts import render, redirect
from .models import Book

# Create your views here.
def home(request):
    books = Book.objects.all()
    return render(request, 'index.html', { "books": books })

def add_book(request):
    if request.method == "POST":
        image = request.FILES.get('image')
        title = request.POST['title']
        author = request.POST['author']
        price = request.POST['price']

        book = Book.objects.create(image=image, title=title, author=author, price=price)
        book.save()

        return redirect('/')
    
    return render(request, 'add_book.html')
    