from django.http import HttpResponse
from django.shortcuts import render
from demo.models import User

def index(request):
    return render(request, 'index.html', {'page': 'index', 'message': ''})

def content(request):
    if 'user' in request.session:
        return render(request, 'content.html', {'page': 'content', 'message': ''})
    else:
        return render(request, 'index.html', {'page': 'index', 'message': ''})

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'page': 'login', 'message': ''})
    else:
        name = request.POST['username']
        users = User.objects.filter(username__exact=name)
        if users.count() == 0:
            return render(request, 'login.html', {'page': 'login', 'message': 'Username/password incorrect'})
        else:
            request.session['user'] = users[0].fullname
            return render(request, 'content.html', {'page': 'content', 'message': request.session['user'] + ': welcome back!'})

def register(request):
    if not 'user' in request.session:
        return render(request, 'index.html', {'page': 'index', 'message': 'Please login first'})        
    elif request.method == 'GET':
        return render(request, 'register.html', {'page': 'register', 'message': ''})
    else:
        name = request.POST['username']
        users = User.objects.filter(username__exact=name)
        if users.count() > 0:
            return render(request, 'register.html', {'page': 'register', 'message': 'Username is not available'})
        else:
            b = User(username=name, fullname=request.POST['fullname'], password=request.POST['password'])
            b.save()
            return render(request, 'content.html', {'page': 'content', 'message': 'New user registered: ' + request.POST['fullname']})    

def logout(request):
    request.session.flush()
    return render(request, 'index.html', {'page': 'logout', 'message': 'You have been logged out'})
    