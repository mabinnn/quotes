from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from . models import User, Quote

def index(request):
    print "I am the index *********"
    return render(request, 'belt_app/index.html')

def register_logic(request):
    print "This is the registration logic******", request
    postInfo = {
        "first_name": request.POST['first_name'],
        "last_name": request.POST['last_name'],
        "email": request.POST['email'],
        "password": request.POST['password'],
        "confirm_password": request.POST['confirm_password']
    }
    # this block to gather all the error messages gained from the models page. Remember we created an array to list all the error messages?.To loop through every message errors, create a new variable called flags.
    flags = User.marvin.register(postInfo)

    if flags:
        for flag in flags:
            messages.warning(request, flag)
        return redirect('/')
    # If the user meets all conditions to make an account, it will run this else function.
    else:
    # Create an object called user_who. user_who is the instance of the User class. It referes to the whole row of data of a person. Think of a person as a data, and names, email etc are the metadata. Person is the object.
        user_who = User.marvin.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'])
        request.session['id'] = user_who.id
    #user_who.id access the id of the user_who object.
    #to access password of the user, I can use user_who.password.
        return redirect('/success')
        #alwayes redirect a post method. Not render an HTML Page.

def success_logic(request):
    # use the userInstance to access the user on session or whoever logged in using their own user id. SEE register_log function.
    userInstance = User.marvin.get(id=request.session['id'])
    context = {
        "userInstance" : userInstance,
        "messages": Quote.objects.all(),
        "favorites" : Quote.objects.all()
        }
    return render(request,"belt_app/process.html",context)

def verify_logic(request):
    print "This is the Verification def********", request
    email = request.POST['email']
    password = request.POST['password']
    flags = User.marvin.verify(email, password)

    if flags:
        for flag in flags:
            messages.warning(request, flag)
        return redirect('/')

    else:
        # make sure to have an ID that can refer to by running the next two lines of codes.
        current_user = User.marvin.get(email=request.POST['email'])
        request.session['id'] = current_user.id
        return redirect('/success')

def logout(request):
    print "User has logged out! ************ "
    request.session['id'] = 0
    return redirect ('/')


def contribute_logic(request):
    print "User submitted a new quote! ************ ", request
    Quote.objects.create(message=request.POST['message'], quoted_by=request.POST['quoted_by'])
    context = {
        "userInstance": User.marvin.get(id=request.session['id']).first_name,
    }
    return redirect('/success', context)

def add_favorites(request, id):
    print "adding to list"
    context = {
        "favorites" : Quote.objects.all()
    }
    Quote.objects.filter(id=id).delete()
    return redirect('/sucess', context)
