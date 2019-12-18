from django.forms import ModelForm
from BookManage.models import Book
from django import forms
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create the form class.
class BookForm(ModelForm):
    class Meta:
        model =Book
        fields = ['title', 'author','issn', 'vol', 'coverImage', 'status']


