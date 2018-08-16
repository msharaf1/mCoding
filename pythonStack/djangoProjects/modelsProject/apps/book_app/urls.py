from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^createBook', views.createBook, name="createBook"),
    url(r'^createAuthor', views.createAuthor, name="createAuthor"),
    # url(r'^createBook/(?P<id>)', views.createBook)
]