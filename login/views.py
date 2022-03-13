
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm,LoginForm
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login, logout


class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    print(form_class)
    template_name = "registration/signup.html"


def login_view(request):
    context = {'errors': ''}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            uservalue = form.cleaned_data.get("email")
            passvalue = form.cleaned_data.get("password")

            user = authenticate(username=uservalue, password = passvalue)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                context = {'form': form,
                           'error': 'Не верная комбинация эл. почты и пароля.'}
                return render(request, 'registration/login.html', context)
    else:
        form = LoginForm()
        context = {'form': form}
        return render(request, 'registration/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')
