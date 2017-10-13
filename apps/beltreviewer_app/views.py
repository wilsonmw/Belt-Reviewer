from django.shortcuts import render, redirect

from .models import User

from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'beltreviewer_app/index.html')

def register(request):
    results = User.objects.registerVal(request.POST)
    for error in results['errors']:
        messages.error(request, error)
    return redirect('/')

def login(request):
    results = User.objects.loginVal(request.POST)
    if results['status']==False:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/')
    else:
        request.session['first_name']=User.objects.get(id=results['id']).first_name
        print request.session['first_name']
        return redirect('/books')


