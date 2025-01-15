from django.shortcuts import render, redirect

from .forms import UserRegistrationForm, UserUpdateForm, ResetPasswordForm, UserLoginForm
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
User = get_user_model()


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email').strip().lower()
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=email, email=email, password=password)
                login(request, user)
                return redirect('business_onboarding')

    else:
        form = UserRegistrationForm()
        return render(request, 'users/register.html', {'form':form})


def user_login(request):
    if request.method == 'POST':
        # email = request.POST.get('email')
        # password = request.POST.get('password')
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, username=email, password=password)

            if user:
                login(request, user)
                messages.success(request, "You're logged in!")
                return redirect('business_onboarding')
            else:
                messages.error(request, 'Wrong email or password')
                return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
            return render(request, 'users/login.html', {'form': form})
    else:
        form = UserLoginForm()
        return render(request, 'users/login.html', {'form':form})


@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def view_profile(request):
    user = request.user
    if request.method == 'POST':
        update_form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if update_form.is_valid():
            update_form.save()
            messages.success(request, 'Profile updated successfully!.')
        return redirect('profile')
    else:
        update_form = UserUpdateForm(instance=user)

        return render(request, 'users/profile.html', {'update_form':update_form})

@login_required(login_url='login')
def reset_password(request):

    user = request.user
    if request.method == 'POST':
        form = ResetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            login(request, user)
            return redirect('profile')
        else:
            for error in list(form.errors.values()):
                        messages.error(request, error)
            return redirect('password')
    else:
        form = ResetPasswordForm(user)
        return render(request, 'users/password_reset.html', {'form':form})