from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from fruitCoop.forms import *
from django.contrib.auth.models import *
from fruitCoop.models import *
from django.contrib.auth.decorators import login_required


def homepage(request):
    return render(request, 'homepage.html')

@login_required
def dashboard(request):
    user = User.objects.get(id=request.user.id)
    return render(request, 'dashboard.html', locals())


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

                return redirect('dashboard')
            else:
                error=True
                #ErrorMessage = "Username ou mot de passe incorrect"
    else:
        form= SignInForm()
    return render(request, 'signin.html', locals())


def logout_user(request):
    logout(request)
    return render(request, 'homepage.html')


#Creation d'un compte producteur
def signup_producteur(request):
    if request.method == 'POST':
        form = SignUpFormMember(request.POST)
        if form.is_valid():
            form.save() #Sauvegarde/Creation d'un utilisateur de base
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password) #Authentification de l'utilisateur
            Utilisateur = User.objects.get(username=username)
            producteur = Member(nummember=Utilisateur, birthdaydatemember=form.cleaned_data.get('datenaissanceproducteur'), telephonemember=form.cleaned_data.get('telephoneproducteur'), postalcodemember=form.cleaned_data.get('codepostalproducteur'), citymember=form.cleaned_data.get('villeproducteur'), address1member=form.cleaned_data.get('adresse1producteur'), address2member=form.cleaned_data.get('adresse2producteur'), nummember_id=Utilisateur.id)
            producteur.save()  # Sauvegarde du client
            login(request, user) #Connexion au site
            estProducteur = True
            request.session['estProducteur'] = estProducteur  # On mémorise le fait que c'est un producteur en session
            return render(request, 'homepage.html')
    else:
        form = SignUpFormMember(request.POST)
    return render(request, 'signup_producteur.html', {'formProducteur': form})




#---------------- VIEWS DE LECTURE  ----------------


@login_required
def read_myaccount(request):
    utilisateur = User.objects.get(id=request.user.id)
    member = Member.objects.get(nummember=request.user.id)
    return render(request, 'myaccount.html',locals())


@login_required
def read_myexport(request):
    user = User.objects.get(id=request.user.id)
    member = Member.objects.get(nummember=user)
    exports = Exporter.objects.filter(nummember=member) #Résultat ordonné
    return render(request, 'myexport.html', locals())

@login_required
def read_myslot(request):
    user = User.objects.get(id=request.user.id)
    member = Member.objects.get(nummember=user)
    slots = Member.objects.filter(nummember=member).order_by(
        'begindateslot')  # Résultat ordonné
    return render(request, 'myslot.html', locals())

@login_required
def read_myroom(request):
    user = User.objects.get(id=request.user.id)
    member = Member.objects.get(nummember=user)
    room = Affecter.objects.filter(nummember=member)
    return render(request, 'myroom.html', locals())

@login_required
def read_memberbyroom(request):
    user = User.objects.get(id=request.user.id)
    member = Member.objects.get(nummember=user)
    room = Affecter.objects.filter(nummember=member)
    numroom = Room.objects.filter(numroom=room)
    listMember = Affecter.objects.filter(numroom=numroom)
    return render(request, 'read_memberbyroom.html', locals())



