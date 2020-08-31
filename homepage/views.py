from homepage.forms import LoginForm
from homepage.forms import SignupForm
from homepage.models import myuser

from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import reverse


@login_required
def homepage_view(request):
    return render(request, 'index.html', {
        "model": settings.AUTH_USER_MODEL,
        "display_name": request.user.get_full_name()
    })


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = myuser.objects.create_user(
                username=data.get('username'),
                password=data.get('password')
            )

            login(request, user)
            return HttpResponseRedirect(reverse("home"))

    form = SignupForm()
    return render(request, 'generic_form.html', {"form": form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get(
                'username'), password=data.get('password'))
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse("home"))
                )

    form = LoginForm()
    return render(request, 'generic_form.html', {
        "form": form,
        "login": True,
    })


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))
