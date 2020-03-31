from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html', {'password':'testnumero_uno'})

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    #create list of lowercase letters
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    #get length of password (second number is default)
    length = int(request.GET.get('length', 12))

    #initial password is blank
    the_password = ''

    #loop through length of password wanted and add random letter to end
    for x in range(length):
        the_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password':the_password})
