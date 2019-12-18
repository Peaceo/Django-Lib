from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from BookManage.models import Book
from BookManage.forms import BookForm
from django.contrib.auth import logout, authenticate
from django.contrib.auth.forms import UserCreationForm



# Create your views here.
def viewBook(request):
    all_Book = Book.objects.all()
    return render(request, 'admin.html', {'Book':all_Book})

def new(request):
    form=BookForm()
    return render(request,'newbook.html',{'form':form})

def forms(request):
    form = BookForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/viewBook/')
    else:
        return render(request, 'newbook.html', {'form': form})

def deleteBook(request, book_id):
    delete_book = Book.objects.get(id = book_id)  
    delete_book.delete()
    return HttpResponseRedirect('/viewBook/') 

def myBook(request):
    all_Book = Book.objects.all()
    return render(request, 'mybooks.html', {'Book':all_Book})

def details(request, book_id):
    state_book = Book.objects.get(id = book_id)
    return render(request, 'statebook.html', {'Book':state_book})

def detail(request, book_id):
    book_detail = Book.objects.get(id = book_id)
    return render(request, 'details.html', {'Book':book_detail})

def edit(request,book_id):
    book = Book.objects.get(id=book_id)
    book_form = BookForm(instance = book)
    return render(request, 'statebook.html', { 'form':book_form, "book": book})

def update(request,book_id):
    book = Book.objects.get(id = book_id)
    book_form = BookForm(request.POST, instance = book)
    if book_form.is_valid():
        book_form.save()
        return HttpResponseRedirect('/viewBook/') 
    else:
        return render(request, 'statebook.html', {'form': book_form, 'book': book})
 
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            return redirect('/viewBook/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})