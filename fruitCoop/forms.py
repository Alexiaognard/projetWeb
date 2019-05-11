from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


#Formulaire pour la connexion au site
class SignInForm(forms.Form):
    username = forms.CharField(max_length=254)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

#Formulaire de creation d'un compte producteur
class SignUpFormProducteur(UserCreationForm):
    datenaissanceproducteur = forms.DateField(label="Date de naissance",widget=forms.SelectDateWidget(years=range(1900, 2100)))
    telephoneproducteur = forms.CharField(label="Numéro de téléphone")
    codepostalproducteur = forms.IntegerField(label="Code postal")
    villeproducteur= forms.CharField(label="Ville")
    adresse1producteur = forms.CharField(label="Adresse1")
    adresse2producteur = forms.CharField(label="Adresse2")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'datenaissanceproducteur', 'email', 'telephoneproducteur',
                      'codepostalproducteur', 'villeproducteur', 'adresse1producteur', 'adresse2producteur', 'password1', 'password2')