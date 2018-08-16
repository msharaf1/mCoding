from django.db import models

class Validator(models.Manager):
    
    def validateBook(self, postData):

        errorBookMessage = {}
    
        if len(postData["bookName"]) < 2: #this has to match with the html form name=value
            errorBookMessage["validName"]= "Please type a valid Name"
        if len(postData["description"]) <2:
            errorBookMessage["validDescription"]=("Please add more information about the book")
        return errorBookMessage
    
    def validateAuthor(self, postData):
        errorAuthorMessage = {}
        if len(postData["firstName"]) <2:
            errorAuthorMessage = "Please type a valid first Name"
        if len(postData["lastName"]) <2:
            errorAuthorMessage = "Please type a valid last Name"
        if len(postData["email"]) <2:
            errorAuthorMessage="please enter a valid Email."
        return errorAuthorMessage


class Book(models.Model):
    bookName = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects= Validator()

    def __repr__(self):
        return f"Book Name: {self.bookName} Description: {self.description}"

class Author(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    authorBooks = models.ManyToManyField(Book, related_name="bookAuthors")
    
    # authorToBook = models.ForeignKey(Book, related_name = "bookToAuthor", on_delete = models.CASCADE)
    

    # Author.objects.get(id=1).authorBooks.add(Book.objects.get(id=1))
    # Book.objects.get(id=1).bookAuthors.add(Author.objects.get(id=1))

    objects=Validator()
    
    def __repr__(self):
        return f"First Name: {self.firstName} Last Name: {self.lastName} Email: {self.email}"

    # book = models.ForeignKey(Book, related_name="bookToAuthors")
    # for author in Book.bookAuthors.all()