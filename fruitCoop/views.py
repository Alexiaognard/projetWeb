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
    return render(request, 'dashboard.html')

@login_required
def addroom(request):
    user = User.objects.get(id=request.user.id)
    member = Member.objects.get(nummember=request.user.id)
    room = Appartenir.objects.filter(nummember=member.nummember)
    myroom=[]
    for rooms in room:
       myroom.append(rooms)
    if myroom==[]:

        if request.method == 'POST':
            form = addRoomForm(request.POST)
            if form.is_valid():
                nameroom= form.cleaned_data('nameroom')
                room=Room.objects.get(nameroom=nameroom)
                appartient=Appartenir(nummember=member.nummember,numroom=room.numroom)
                appartient.save()
                return redirect('dashboard')
        else:
            form=addRoomForm()
    return render(request, 'addroom.html', {'formAddRoom': form})




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
            form.save()  # Sauvegarde/Creation d'un utilisateur de base
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # Authentification de l'utilisateur
            Utilisateur = User.objects.get(username=username)
            producteur = Member(nummember=Utilisateur,
                                firstnamemember=form.cleaned_data.get('first_name'),
                                lastnamemember=form.cleaned_data.get('last_name'),
                                birthdaydatemember=form.cleaned_data.get('datenaissanceproducteur'),
                                telephonemember=form.cleaned_data.get('telephoneproducteur'),
                                postalcodemember=form.cleaned_data.get('codepostalproducteur'),
                                citymember=form.cleaned_data.get('villeproducteur'),
                                address1member=form.cleaned_data.get('adresse1producteur'),
                                address2member=form.cleaned_data.get('adresse2producteur'), nummember_id=Utilisateur.id)
            producteur.save()  # Sauvegarde du producteur
            login(request, user)  # Connexion au site
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
def read_rooms(request):

    room=Room.objects.filter(nameroom=nameroom)
    return render(request, 'readroom.html', locals())

@login_required
def read_memberbyroom(request, nameroom):
    numroom = Room.objects.filter(nameroom=nameroom)
    listMember = Appartenir.objects.filter(numroom=numroom)
    return render(request, 'read_memberbyroom.html', locals())


#---------------- VIEWS DE MODIFICATION  ----------------

@login_required
def update_member(request):
    user = User.objects.get(id=request.user.id)
    member = Member.objects.get(nummember=request.user.id)
    if request.method == "POST":
        form = UpdateMemberForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.save()
            member.birthdaydatemember = form.cleaned_data.get('datenaissanceproducteur')
            member.telephonemember = form.cleaned_data.get('telephoneproducteur')
            member.postalcodemember = form.cleaned_data.get('codepostalproducteur')
            member.citymember = form.cleaned_data.get('villeproducteur')
            member.address1member = form.cleaned_data.get('adresse1producteur')
            member.address2member = form.cleaned_data.get('adresse2producteur')
            member.save()
            return read_myaccount(request)
        else:
            date = str(member.birthdaydatemember.year)+"-"+str(member.birthdaydatemember.month)+"-"+str(member.birthdaydatemember.day) #Permet d'avoir le bon format de date pour le input : type=date , du formulaire
            member.birthdaydatemember = date
    return render(request, 'updatemember.html', locals())



