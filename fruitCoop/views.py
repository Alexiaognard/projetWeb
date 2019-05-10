from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    return render(request, 'accueil.html')

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
                groupe = User.objects.filter(groups__name='producteur', id=user.id) #On cherche si notre utilisateur est un producteur
                if not groupe: #Si aucun objet n'est retourné, il n'est pas producteur
                    estClient = False
                else:           #Sinon, c'est un producteur
                    estClient =True
                request.session['estClient'] = estClient #On mémorise cette information
                request = init_panier(request)
                request = init_reservation(request) #On initilise le panier et le panier_reservation de l'utilisateur

                if estClient:
                    return redirect('homepage')
                else:
                    return redirect('gestion/dashboard/')
            else:
                error=True
                #ErrorMessage = "Username ou mot de passe incorrect"
    else:
        form= SignInForm()
    return render(request, 'signin.html', locals())


def logout_user(request):
    logout(request)
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')