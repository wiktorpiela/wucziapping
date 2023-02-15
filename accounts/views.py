from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from .func import validate_email
from verify_email.email_handler import send_verification_email
from .forms import RegisterForm

def login_user(request):
    if request.method == "GET":
        return render(request, "login_user.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        username_exist = User.objects.filter(username=username).exists()
        if username_exist == False:
            message = f"Użytkownik {username} nie istnieje. Spróbuj ponownie."
            return render(request, "login_user.html", {"noUser":message})
        else:
            user_is_active = User.objects.filter(username=username, is_active = True).exists()
            if user_is_active == False:
                message = f"Konto użytkownika {username} jest nieaktywne. Aktywuj konto, a następnie spróbuj ponownie."
                return render(request, "login_user.html", {"inactiveUser":message})
            else:
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect("accounts:login_user")
                else:
                    message = "Niepoprawne hasło. Sprobuj ponownie lub zresetuj hasło."
                    return render(request, "login_user.html", {"wrongPass":message})

def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    else:
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 == password2:
            try:
                validate_password(password1)
            except ValidationError as exceptions:
                return render(request, "register.html", {"passError":exceptions, "length":len(list(exceptions))})
            else:
                if validate_email(email):
                    username_taken = User.objects.filter(username=username).exists()
                    email_taken = User.objects.filter(email=email).exists()
                    if username_taken:
                        message = f"Nazwa użytkownika {username} jest zajęta. Spróbuj ponownie"
                        return render(request, "register.html", {"usernameTaken":message})
                    elif email_taken:
                        message = f"Adres email {email} jest zajęty. Spróbuj ponownie"
                        return render(request, "register.html", {"emailTaken":message})
                    else:
                        form = RegisterForm(request.POST)
                        inactive_user = send_verification_email(request, form)
                        return redirect("accounts:login_user")
                else:
                    message = "Niepoprawny format adresu email. Spróbuj ponownie."
                    return render(request, "register.html", {"emailError":message})
        else:
            message = "Hasła nie są identyczne. Spróbuj ponownie."
            return render(request, "register.html", {"dontMatch":message})

@login_required
def logout_user(request):
    logout(request)
    return redirect("accounts:login_user")