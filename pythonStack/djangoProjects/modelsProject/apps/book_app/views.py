from django.shortcuts import render, redirect
from .models import Book, Author

def index(request):

    context = {
        "bookData": Book.objects.all(),
        "authorData": Author.objects.all()
    }


    return render(request, "book_app/index.html", context)

def createBook(request, methods=["POST"]):
    Book.objects.create(bookName = request.POST['bookName'], description = request.POST["description"])

    return redirect("/")
    

def createAuthor(request, methods=["POST"]):
    Author.objects.create(firstName = request.POST["firstName"], lastName = request.POST["lastName"], email = request.POST["email"] )
    # Blog.objects.create({{field1}}="{{value}}", {{field2}}="{{value}}", etc)

    # a = Author.objects.get(id=request.POST["bookId"])

    # Author.objects.create(firstName = request.POST["firstName"], lastName = request.POST["lastName"], email = request.POST["email"], authorsid = a)
    
    return redirect("/")

# def createBook(request, id):
