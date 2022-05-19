from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def index(request):
  return render(request, 'index.html')

def signup(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    password2 = request.POST['password2']

    if password == password2:
      pass
    else:
      messages.info(request, 'Passwords do not match')
      return redirect('signup')


  else:
    return render(request, 'signup.html')