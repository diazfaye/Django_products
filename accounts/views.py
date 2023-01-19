from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

User = get_user_model()

# Create your views here.
def signup(request):
    if request.method=="POST":
        # Traiter le formulaire
        # récupérer le username et le mot de passe
        username = request.POST.get("username")
        password = request.POST.get("password")
        address = request.POST.get("address")
        address_mail = request.POST.get("email")
        # créer un utilisateur qu'on va récupérer dans une variable user
        User.objects.create_user(username=username, password=password, address=address, email=address_mail)
        # connecter l'utilisateur
        #login(request, user)
        # retour vers la page d'accueil
        return redirect('index')
    return render(request, 'accounts/signup.html')

def login_user(request):
    if request.method == "POST":
        # récupérer le username et le mot de passe
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        return redirect('signup')
    return render(request, 'accounts/login.html')

def logout_user(request):
    logout(request)
    return redirect('index')
