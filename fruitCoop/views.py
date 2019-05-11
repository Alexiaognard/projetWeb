from django.shortcuts import render, redirect
from django.http import HttpResponse
from fruitCoop.forms import SignUpFormProducteur, SignInForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Permission, User
from fruitCoop.models import Producteur


def homepage(request):
    return render(request, 'dashboard.html')

#---------------- VIEWS DE CONNEXION, DECONNEXION  ----------------


def login_user(request):
    error=False
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            raw_password = form.cleaned_data["password"]
            user = authenticate(username=username, password=raw_password)
            if user:
                login(request,user)

                return redirect('homepage')
            else:
                error=True
                #ErrorMessage = "Username ou mot de passe incorrect"
    else:
        form= SignInForm()
    return render(request, 'signin.html', locals())


def logout_user(request):
    logout(request)
    return render(request, 'index.html')

def read_myaccount(request):
    utilisateur = User.objects.get(id=request.user.id)
    producteur = Producteur.objects.get(numproducteur=request.user.id)
    return render(request, 'myaccount.html', locals())

#Creation d'un compte producteur
def signup_producteur(request):
    if request.method == 'POST':
        form = SignUpFormProducteur(request.POST)
        if form.is_valid():
            form.save() #Sauvegarde/Creation d'un utilisateur de base
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password) #Authentification de l'utilisateur
            Utilisateur = User.objects.get(username=username)
            producteur = Producteur(numproducteur=Utilisateur, datenaissanceproducteur=form.cleaned_data.get('datenaissanceproducteur'), telephoneproducteur=form.cleaned_data.get('telephoneproducteur'), codepostalproducteur=form.cleaned_data.get('codepostalproducteur'), villeproducteur=form.cleaned_data.get('villeproducteur'), adresse1producteur=form.cleaned_data.get('adresse1producteur'), adresse2producteur=form.cleaned_data.get('adresse2producteur'), numproducteur_id=Utilisateur.id)
            producteur.save()  # Sauvegarde du client
            login(request, user) #Connexion au site
            estProducteur = True
            request.session['estProducteur'] = estProducteur  # On mémorise le fait que c'est un client en session

    else:
        form = SignUpFormProducteur(request.POST)
    return render(request, 'signup_producteur.html', {'formProducteur': form})