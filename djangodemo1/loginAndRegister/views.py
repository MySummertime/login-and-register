
from django.urls import reverse
from django.shortcuts import render, HttpResponseRedirect
from . import models
from . import forms


# Create your views here.


def index(req):
    return render(req, 'loginAndRegister/index.html')


def login(req):
    # user has already logged in
    if req.session.get('is_login', None):
        return HttpResponseRedirect('../login/')

    if req.method == 'POST':
        # retrive login_form variable from HTML
        login_form = forms.UserForm(req.POST)
        err = 'User name/password invalid.'
        '''
        username = req.POST.get('username', '')
        password = req.POST.get('password', '')
        '''
        # guarantee the needed values are valid
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            print(username, password)

            try:
                # guarantee user exists in db loginAndRegister_user
                user = models.User.objects.get(name=username)
            except:
                err = 'User is not exist.'
                return render(req, 'loginAndRegister/login.html', locals())
            # guarantee password is correct
            if user.password == password:
                # update session by updating any key
                req.session['is_login'] = True
                req.session['user_id'] = user.id
                req.session['user_name'] = user.name
                return HttpResponseRedirect('../index/')
            else:
                err = 'Invalid password.'
                return render(req, 'loginAndRegister/login.html', locals())
        # the needed values are invalid
        # return a form with entered values, instead of a empty form
        else:
            return render(req, 'loginAndRegister/login.html', locals())
    # req.method == POST: return an empty page
    login_form = forms.UserForm()
    return render(req, 'loginAndRegister/login.html', locals())


def register(req):
    # user has already logged in
    if req.session.get('is_login', None):
        return HttpResponseRedirect('../logout/')

    if req.method == 'POST':
        register_form = forms.RegisterForm(req.POST)
        err = "User name/password invalid."
        # guarantee the needed values are valid
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')
            gender = register_form.cleaned_data.get('gender')

            # password entered respectively are different
            if password1 != password2:
                err = 'Passwords are different'
                return render(req, 'loginAndRegister/register.html', locals())
            else:
                users = models.User.objects.filter(name=username)
                #print(users)
                # user name occupied
                if users:
                    #print('into users')
                    err = 'User name occupied.'
                    return render(req, 'loginAndRegister/register.html', locals())

                emails = models.User.objects.filter(email=email)
                print(emails)
                # email registered
                if emails:
                    print('into emails')
                    err = 'Email registered.'
                    return render(req, 'loginAndRegister/register.html', locals())

                # create a user
                user = models.User()
                user.name = username
                user.password = password1
                user.email = email
                user.gender = gender
                user.save()
                return HttpResponseRedirect('/control/adminSite/')
        # some variables in register_form are invalid
        else:
            return render(req, 'loginAndRegister/register.html', locals())
    # req.method == GET: return an empty page
    register_form = forms.RegisterForm()
    return render(req, 'loginAndRegister/register.html', locals())


def logout(req):
    #print(req.session['is_login'])

    # user hasn't logged in
    if req.session.get('is_login', None):
        # clear session if user had already logged in
        req.session.flush()
        # or
        # del request.session['is_login']
        # del request.session['user_id']
        # del request.session['user_name']
    return HttpResponseRedirect('../login/')