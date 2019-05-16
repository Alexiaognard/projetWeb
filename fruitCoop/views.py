from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from fruitCoop.forms import *
from django.contrib.auth.models import *
from fruitCoop.models import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage


def homepage(request):
    return render(request, 'homepage.html')

@login_required
def dashboard(request):
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
            return render(request, 'dashboard.html')
    else:
        form = SignUpFormMember(request.POST)
    return render(request, 'signup_producteur.html', {'formProducteur': form})




#---------------- VIEWS DE LECTURE  ----------------


@login_required
def read_myaccount(request):
    utilisateur = User.objects.get(id=request.user.id)
    member = Member.objects.get(nummember=utilisateur)
    room=Appartenir.objects.get(nummember=member)
    return render(request, 'myaccount.html',locals())


@login_required
def read_myexport(request):
    user = User.objects.get(id=request.user.id)
    member = Member.objects.get(nummember=user)
    export = Exporter.objects.filter(nummember=member)
    listExport=[]
    for exports in export:
        listExport.append(exports.numexport)

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
    room = Appartenir.objects.filter(nummember=member)
    return render(request, 'read_myroom.html', locals())

@login_required
def read_rooms(request):
    room=Room.objects.all()
    listRoom=[]
    for rooms in room:
        listRoom.append(rooms)
    return render(request, 'readrooms.html', locals())

@login_required
def read_memberbyroom(request):
    user = User.objects.get(id=request.user.id)
    member = Member.objects.get(nummember=user)
    room = Appartenir.objects.get(nummember=member)
    prod = Appartenir.objects.filter(numroom=room.numroom.numroom)
    listMember = []
    for mem in prod:
        utilisateur=User.objects.get(id=mem.nummember.nummember.id)
        membre=Member.objects.get(nummember=utilisateur)
        listMember.append(mem.nummember)

    return render(request, 'read_memberbyroom.html', locals())



#---------------- VIEWS DE CREATION ----------------


@login_required
def addroom(request):
    utilisateur = User.objects.get(id=request.user.id)
    member = Member.objects.get(nummember=utilisateur)
    if request.method == 'POST':
        form = addRoomForm(request.POST)
        if form.is_valid():
            appartient=Appartenir(nummember=member, numroom=form.cleaned_data.get('choice_room'))
            appartient.save()

            return render(request, 'dashboard.html')
    else:
        form= addRoomForm()
    return render(request, 'addroom.html', {'formAddRoom' : form})


@login_required
def create_export(request):
    utilisateur = User.objects.get(id=request.user.id)
    member = Member.objects.get(nummember=utilisateur)
    if request.method == 'POST':
        form = CreateExportForm(request.POST)
        if form.is_valid():
            exportation=Export(dateexport=form.cleaned_data.get('dateexport'),fruitexport=form.cleaned_data.get('fruitexport'),sizeexport=form.cleaned_data.get('sizeexport'),nbpalletexport=form.cleaned_data.get('nbpalletexport'))
            exportation.save()
            exporter=Exporter(nummember=member,numexport=exportation)
            exporter.save()

            return render(request, 'myexport.html')
    form = CreateExportForm()
    return render(request, 'create_export.html', {'formCreateExport':form})


#---------------- VIEWS DE MODIFICATION  ----------------

@login_required
def update_member(request):
    user = User.objects.get(id=request.user.id)
    member = Member.objects.get(nummember=request.user.id)
    form=UpdateMemberForm()
    if request.method == "POST":
        form = UpdateMemberForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.save()
            member.telephonemember = form.cleaned_data.get('telephoneproducteur')
            member.postalcodemember = form.cleaned_data.get('codepostalproducteur')
            member.citymember = form.cleaned_data.get('villeproducteur')
            member.address1member = form.cleaned_data.get('adresse1producteur')
            member.address2member = form.cleaned_data.get('adresse2producteur')
            member.save()
            return read_myaccount(request)

    return render(request, 'updatemember.html')

@login_required
def update_myexport(request,numexport):
    export=Export.objects.get(numexport=numexport)
    if request.method == "POST":
        form = UpdateExportForm(request.POST)
        if form.is_valid():
            export.dateexport = form.cleaned_data.get('dateexport')
            export.fruitexport = form.cleaned_data.get('fruitexport')
            export.sizeexport = form.cleaned_data.get('sizeexport')
            export.nbpalletexport = form.cleaned_data.get('nbpalletexport')
            export.save()
            return render(request, 'myexport.html')

    return render(request, 'update_myexport.html')



#---------------- VIEWS DE RECHERCHE  ----------------

@login_required
def search(request, keyword=None, page=1):
    #keyword et page sont utilisé lorsque l'utilisateur fait défiler les pages, par défaut ils valent respectivement None et 1
    recherche = request.POST.get('recherche') #On récupère la recherche de l'utilisateur qui nous est envoyé en requete POST
    if keyword is None : #Si la recherche est Vide
        if not recherche:
            return redirect('/') #Redirection vers la page d'accueil si aucun champ de recherche
        else:
            members = Member.objects.filter(firstnamemember__icontains=recherche)
            if not members:
                members_all = Member.objects.filter(lastnamemember__icontains=recherche)


            member = pagination(members,page)
            return render(request, 'search_members.html', locals())
    else:

        members = Member.objects.filter(firstnamemember__icontains=recherche)
        if not members:
            members_all = Member.objects.filter(lastnamemember__icontains=recherche)

        recherche=keyword #On passe la recherche à travers les différentes pages de la pagination

        member = pagination(members, page)
        return render(request, 'search_members.html', locals())


def pagination(liste,nb_page):
    paginator = Paginator(liste, 2)  # On affiche 2 produit par page
    try:
        member = paginator.page(nb_page)
    except EmptyPage:
        member = paginator.page(paginator.num_pages)

    return member
