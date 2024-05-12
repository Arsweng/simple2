from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Book
from .forms import Form
from django.contrib.auth.decorators import login_required
@login_required(login_url = 'users:login')
def allbooks(request):
    books = Book.objects.all()
    return render(request, 'books/books.html',{ 'books':books })

@login_required(login_url = 'users:login')
def onebook(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'books/book.html',{ 'book': book })


@login_required(login_url = 'users:login')


def upload(request):
    if request.method == 'POST':
        form = Form(request.POST, request.FILES)

        if form.is_valid():
            title = form.cleaned_data['title']
            pub_date = form.cleaned_data['pub_date']
            price = form.cleaned_data['price']
            description = form.cleaned_data['description']
            banner = request.FILES.get('banner')
            
            # Assuming you have a ForeignKey relationship between Book and User model
            if request.user.is_authenticated:
                author = request.user  # Use the authenticated user as the author
            else:
                author = None  # If user is not authenticated, set author to None or handle differently
            
            new_book = Book.objects.create(
                title=title,
                author=author,
                pub_date=pub_date,
                price=price,
                description=description,
                banner=banner,
            )
            print('Book saved successfully')
            return redirect('books:allbooks')
        else:
            print('Form is not valid:', form.errors)
    else:
        form = Form()
    

    print(request.user.get_full_name() ,'h')

    return render(request, 'books/upload.html',{  'form':form})
