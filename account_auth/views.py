from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login as auth_login


def signup(request):
    if request.method == 'POST':
        form_s = SignUpForm(request.POST)
        if form_s.is_valid():
            user = form_s.save(commit=False)
            user.is_staff = False
            user.save()
            auth_login(request, user)
            return redirect('serialize')
        print("ВСЕ ПРОШЛО УСПЕШНО")
    else:
        form_s = SignUpForm()
    return render(request, 'account/signup.html', context={'form_s': form_s})
