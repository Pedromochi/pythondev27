from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, "generator/home.html")

def about(request):
    return render(request, "generator/about.html")

# password generator
def password(request):

    characters = list("abcjedjddwdwdyrirrerez")

    if request.GET.get('uppercase'):
        characters.extend(list("ABCJEDJDDWDWDYRIRREREZ"))

    if request.GET.get('special'):
        characters.extend(list("12344556777889866878556635"))

    if request.GET.get('numbers'):
        characters.extend(list("ABCJEDJDDWDWDYRIRREREZ"))

    length = int(request.GET.get('length', 12))

    thepassword = ""
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, "generator/password.html", {"password": thepassword})

