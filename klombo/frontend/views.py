# frontend/views.py
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

#from .models import Image
#from .models import Video
#from .models import Ig


import requests
import json
from datetime import datetime
import re

data = {}

def check_login( request ):

    from .models import LoginCookie

    if 'logindata' in request.session:

        if request.session['logindata']:

            logindata = request.session['logindata']
            query = LoginCookie.objects.filter( data = logindata )

            if len( query ) == 1:

                for cookie in query:

                    enc = make_password( cookie['username'] )
                    result = check_password( logindata, enc ) 
                    
                    if result:

                        return True

    return False

def test( request ):
    # user = User.objects.create(
    #    email=validated_data['email'],
    #    username=validated_data['username'],
    #    password = make_password(validated_data['password'])
    password = 'password'
    enc = make_password(password)
    # enc = 'pbkdf2_sha256$320000$h6NW2mQOzDNSOT7ebx7rvs$OAThdSiFcQxfGbSQgycQDXCRnSwIGBINpzUFiOkpI1M='
    result = check_password(password, enc)
    return HttpResponse( '<h1>Password</h1><br><h1>' + enc + '</h1><br><h1>' + str(result) + '</h1>' )

def login_method( request ):
    from .models import User
    from .models import LoginCookie
    if request.method == 'POST':

        form = request.POST

        if form.get('username'):

            username = form.get('username')

            if form.get('password'):

                password = form.get('password')
                enc = make_password(password)
                query = User.objects.filter( username = username, password = enc )

                if len( query ) > 0:
                    logindata= make_password( username )
                    request.session['logindata'] = logindata
                    b = LoginCookie.objects.create( data = logindata, username = username )
                    b.Save()

def register_method( request ):

    array = {
        'username',
        'password',
        'password2',
        'firstname',
        'lastname',
        'contact',
    }

    from .models import User
    from .models import LoginCookie

    if request.method == 'POST':

        form = request.POST
        username = ''
        password = ''
        password2 = ''
        firstname = ''
        lastname = ''
        contact = ''

        for key in array:

            if form[key]:
                username = form[key]

        if password != '' and password == password2:

            if username != '':

                if len(username)>=6 and len(password)>=8:
                    
                    logindata= make_password( username )
                    enc = make_password( password )
                    a = User.objects.create( username = username, password = enc, firstname = firstname, lastname = lastname, contact = contact )
                    a.Save()
                    b = LoginCookie.objects.create( data = logindata, username = username )
                    b.Save()

    return redirect('index')

def index( request ):

    if check_login( request ):

        return render( request, 'frontend/index.html', data )

    return render( request, 'frontend/welcome.html', data )

def signin( request ):
    
    return render( request, 'frontend/sign.html', data )

def signup( request ):
    
    return render( request, 'frontend/sign.html', data )
	
