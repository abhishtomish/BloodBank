from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm
from blood.models import Blood
# Create your views here.

def register(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()    # if all the data provided are valid it will save the form adding the user to the database.
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('dashboard')
        else:
            context['registration_form'] = form     # here form is not valid
    else:
        form = RegistrationForm()   # here also form is not valid
    context['registration_form'] = form
    return render(request, 'account/register.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')

def dashboard(request):
    context = {}
    blood = Blood.objects.all()
    context['blood'] = blood
    return render(request, 'account/dashboard.html', context)

def login_view(request):

    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("dashboard")
    
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("dashboard")
    
    else:
        form = AccountAuthenticationForm()

    
    context['login_form'] = form

    return render(request, 'account/login.html', context)


def update_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    context = {}

    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AccountUpdateForm(
            initial={
                "email":request.user.email,
                "username":request.user.username
            }
        )
    
    context['update_form'] = form
    return render(request, 'account/update.html', context)
