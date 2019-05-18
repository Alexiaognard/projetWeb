from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from fruitCoop.forms import *
from django.contrib.auth.models import *
from fruitCoop.models import *
from django.core.paginator import Paginator, EmptyPage



def homepage(request):
    return render(request, 'homepage.html')


def dashboard(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        member = Member.objects.get(nummember=user)
        return render(request, 'dashboard.html',locals())
    else:
        return render(request, 'homepage.html')





#---------------- VIEWS DE CONNEXION, DECONNEXION  ----------------


def login_user(request):
    error=False
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            raw_password = form.cleaned_data["password"]
            user = authenticate(username=username, password=raw_password)
            if user is not None and user.is_active:
                login(request,user)
                return dashboard(request)

            else:
                error=True
                #ErrorMessage = "Username ou mot de passe incorrect"
    else:
        form= SignInForm()
    return render(request, 'signin.html', locals())


def logout_user(request):
    logout(request)
    return homepage(request)


#Creation d'un compte producteur
def signup_producteur(request):
    if request.method == 'POST':
        form = SignUpFormMember(request.POST, request.FILES)
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
                                address2member=form.cleaned_data.get('adresse2producteur'), nummember_id=Utilisateur.id,
                                photomember=form.cleaned_data.get('photomember'))
            producteur.save()  # Sauvegarde du producteur
            login(request, user)  # Connexion au site
            estProducteur = True

            request.session['estProducteur'] = estProducteur  # On mémorise le fait que c'est un producteur en session
            return render(request, 'dashboard.html')
    else:
        form = SignUpFormMember(request.POST)
    return render(request, 'signup_producteur.html', {'formProducteur': form})




#---------------- VIEWS DE LECTURE  ----------------


def read_myaccount(request):

    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        member = Member.objects.get(nummember=user)
        try:
            room=Appartenir.objects.get(nummember=member)
        except:
            return redirect('addRoom')
        else:
            room = Appartenir.objects.get(nummember=member)
    else:
        return redirect('homepage')
    return render(request, 'read/myaccount.html',locals())



def read_myexport(request):
    if request.user.is_authenticated :
        user = User.objects.get(id=request.user.id)
        member = Member.objects.get(nummember=user)
        export = Exporter.objects.filter(nummember=member)
        listExport=[]
        for exports in export:
            listExport.append(exports.numexport)
    else:
        return redirect('homepage')

    return render(request, 'read/myexport.html', locals())


def read_exportform(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        member = Member.objects.get(nummember=user)
        exportform = Remplir.objects.filter(nummember=member)
        listFiche = []
        for exports in exportform:
            listFiche.append(exports.numexportform)

    else:
        return redirect('homepage')

    return render(request, 'read/read_exportform.html', locals())




def read_myroom(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        member = Member.objects.get(nummember=user)
        try :
            app=Appartenir.objects.get(nummember=member)
        except:
            return redirect('addRoom')
        else:
            app = Appartenir.objects.get(nummember=member)
            room=Room.objects.get(numroom=app.numroom.numroom)
    else:
        return redirect('homepage')

    return render(request, 'read/read_myroom.html', locals())


def read_rooms(request):
    if request.user.is_authenticated:
        room=Room.objects.all()
        listRoom=[]
        for rooms in room:
            listRoom.append(rooms)

    else:
        return redirect('homepage')
    return render(request, 'read/readrooms.html', locals())


def read_memberbyroom(request,numroom):
    if request.user.is_authenticated:
        prod = Appartenir.objects.filter(numroom=numroom)
        listMember = []
        for mem in prod:
            listMember.append(mem.nummember)
    else:
        return redirect('homepage')

    return render(request, 'read/read_memberbyroom.html', locals())



#---------------- VIEWS DE CREATION ----------------



def addroom(request):
    if request.user.is_authenticated:
        utilisateur = User.objects.get(id=request.user.id)
        member = Member.objects.get(nummember=utilisateur)
        if request.method == 'POST':
            form = addRoomForm(request.POST)
            if form.is_valid():
                appartient=Appartenir(nummember=member, numroom=form.cleaned_data.get('choice_room'))
                try:
                    appartient.save()
                except:
                    return render(request, 'read/read_myroom.html')
        else:
            form= addRoomForm()
    else:
        return redirect('homepage')

    return render(request, 'addroom.html', {'formAddRoom' : form})



def create_export(request):
    if request.user.is_authenticated:
        utilisateur = User.objects.get(id=request.user.id)
        member = Member.objects.get(nummember=utilisateur)
        if request.method == 'POST':
            form = CreateExportForm(request.POST)
            if form.is_valid():
                numform = form.cleaned_data.get('numexportform')
                try:
                    numero = Exportform.objects.get(numform=numform)
                    exportation=Export(dateexport=form.cleaned_data.get('dateexport'),fruitexport=form.cleaned_data.get('fruitexport'),
                                   sizeexport=form.cleaned_data.get('sizeexport'),nbpalletexport=form.cleaned_data.get('nbpalletexport'),
                                   numexportform=numero)
                    exportation.save()
                except:
                    erreur=True
                    return render(request, 'create/create_export.html', {'formCreateExport':form}, erreur)
                else:
                    exporter=Exporter(nummember=member,numexport=exportation)
                    exporter.save()

                return read_myexport(request)
        form = CreateExportForm()
    else:
        return redirect('homepage')
    return render(request, 'create/create_export.html', {'formCreateExport':form})


def create_exportform(request):
    if request.user.is_authenticated:
        utilisateur = User.objects.get(id=request.user.id)
        member = Member.objects.get(nummember=utilisateur)
        if request.method == 'POST':
            form = CreateFicheForm(request.POST)
            if form.is_valid():
                fiche=Exportform(brixform=form.cleaned_data.get('brixform'),fruitform=form.cleaned_data.get('fruitform'),
                                   maturityform=form.cleaned_data.get('maturityform'),nbfruitform=form.cleaned_data.get('nbfruitform'),
                                   parcelleform=form.cleaned_data.get('parcelleform'))
                fiche.save()
                remplir=Remplir(nummember=member,numexportform=fiche)
                remplir.save()

                return read_exportform(request)
        form = CreateFicheForm()
    else:
        return redirect('homepage')
    return render(request, 'create/create_exportform.html', {'formCreateExportForm':form})


#---------------- VIEWS DELETE  ----------------


def delete_myexport(request, numexport):
    if request.user.is_authenticated:
        export = get_object_or_404(Export, numexport=numexport)
        if request.method == 'POST':
            Export.objects.get(numexport = numexport).delete()
            return read_myexport(request)
    else:
        return redirect('homepage')

    return render(request, 'delete/deleteView.html')


def delete_myexportform(request, numform):
    if request.user.is_authenticated:
        exportform = get_object_or_404(Exportform, numform=numform)
        if request.method == 'POST':
            Exportform.objects.get(numform = numform).delete()
            return read_exportform(request)
    else:
        return redirect('homepage')

    return render(request, 'delete/deleteView.html')



#---------------- VIEWS UPDATE  ----------------


def update_member(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        member = Member.objects.get(nummember=request.user.id)
        if request.method == "POST":
            form = UpdateMemberForm(request.POST, request.FILES)
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
                member.photomember = form.cleaned_data.get('photomember')
                member.save()
                return read_myaccount(request)
        form = UpdateMemberForm()
    else:
        return redirect('homepage')

    return render(request, 'update/updatemember.html', {'formProducteur':form})


def update_myexport(request,numexport):
    if request.user.is_authenticated:
        export=Export.objects.get(numexport=numexport)
        if request.method == "POST":
            form = UpdateExportForm(request.POST)
            if form.is_valid():
                export.fruitexport = form.cleaned_data.get('fruitexport')
                export.sizeexport = form.cleaned_data.get('sizeexport')
                export.nbpalletexport = form.cleaned_data.get('nbpalletexport')
                export.save()
                return read_myexport(request)
        form = UpdateExportForm()
    else:
        return redirect('homepage')

    return render(request, 'update/update_myexport.html', {'formExport':form})


def update_myexportform(request,numform):
    if request.user.is_authenticated:
        export=Exportform.objects.get(numform=numform)
        if request.method == "POST":
            form = UpdateFicheForm(request.POST)
            if form.is_valid():
                export.brixform = form.cleaned_data.get('brixform')
                export.fruitform = form.cleaned_data.get('fruitform')
                export.maturityform = form.cleaned_data.get('maturityform')
                export.nbfruitform = form.cleaned_data.get('nbfruitform')
                export.parcelleform = form.cleaned_data.get('parcelleform')
                export.save()
                return read_exportform(request)
        form = UpdateFicheForm()
    else:
        return redirect('homepage')

    return render(request, 'update/update_exportform.html',{'formExport':form})

#---------------- VIEWS DE RECHERCHE  ----------------


def search(request, keyword=None, page=1):
    #keyword et page sont utilisé lorsque l'utilisateur fait défiler les pages, par défaut ils valent respectivement None et 1
    recherche = request.POST.get('recherche') #On récupère la recherche de l'utilisateur qui nous est envoyé en requete POST
    if keyword is None : #Si la recherche est Vide
        if not recherche:
            return redirect('/') #Redirection vers la page d'accueil si aucun champ de recherche
        else:
            members = Member.objects.filter(firstnamemember__icontains=recherche).order_by('nummember')
            membre = Member.objects.filter(lastnamemember__icontains=recherche).order_by('nummember')
            listMember=[]
            for mem in members:
                listMember.append(mem)
            for mem in membre:
                listMember.append(mem)

            member = pagination(members,page)


            return render(request, 'search_members.html', locals())
    else:

        members = Member.objects.filter(firstnamemember__icontains=recherche).order_by('nummember')
        membre = Member.objects.filter(lastnamemember__icontains=recherche).order_by('nummember')
        listMember = []
        for mem in members:
            listMember.append(mem)
        for mem in membre:
            listMember.append(mem)


        recherche=keyword #On passe la recherche à travers les différentes pages de la pagination

        member = pagination(members, page)
        return render(request, 'search_members.html', locals())


def pagination(liste,nb_page):
    paginator = Paginator(liste, 5)  # On affiche 5 membres par page
    try:
        member = paginator.page(nb_page)
    except EmptyPage:
        member = paginator.page(paginator.num_pages)

    return member

