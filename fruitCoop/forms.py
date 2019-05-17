from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelChoiceField
from fruitCoop.models import *
from django.core.files.uploadedfile import SimpleUploadedFile

#Formulaire pour la connexion au site
class SignInForm(forms.Form):
    username = forms.CharField(max_length=254)
    password = forms.CharField( widget=forms.PasswordInput)

class RoomChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.nameroom

#Formulaire de creation d'un compte producteur
class SignUpFormMember(UserCreationForm):
    datenaissanceproducteur = forms.DateField(label="Date de naissance",widget=forms.SelectDateWidget(years=range(1900, 2100)))
    telephoneproducteur = forms.CharField(label="Numéro de téléphone")
    codepostalproducteur = forms.IntegerField(label="Code postal")
    villeproducteur= forms.CharField(label="Ville")
    adresse1producteur = forms.CharField(label="Adresse1")
    adresse2producteur = forms.CharField(label="Adresse2 (Mettre un espace si le champs est vide)")
    photomember = forms.ImageField(label='Votre photo')


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'datenaissanceproducteur', 'email', 'telephoneproducteur',
                      'codepostalproducteur', 'villeproducteur', 'adresse1producteur', 'adresse2producteur','photomember','password1', 'password2')


class UpdateMemberForm(forms.Form):
    first_name = forms.CharField(label = "Prénom")
    last_name = forms.CharField(label = "Nom")
    email = forms.EmailField(label = "Adresse électronique")
    telephoneproducteur = forms.CharField(label="Numéro de téléphone")
    codepostalproducteur = forms.IntegerField(label="Code postal")
    villeproducteur = forms.CharField(label="Ville")
    adresse1producteur = forms.CharField(label="Adresse1")
    adresse2producteur = forms.CharField(label="Adresse2")
    photomember = forms.ImageField(label="Votre photo")

class addRoomForm(forms.Form):
    choice_room = RoomChoiceField(queryset=Room.objects.all(), to_field_name='numroom', label="Local")

class CreateExportForm(forms.Form):
    dateexport = forms.DateField(label="Date d'exportation",widget=forms.SelectDateWidget(years=range(2019, 2100)))
    fruitexport = forms.CharField(label="Fruit exporté")
    sizeexport = forms.IntegerField(label="Calibre exporté")
    nbpalletexport = forms.IntegerField(label="Nombre de palettes exportées")
    numexportform = forms.IntegerField(label="Numéro de fiche d'exportation")
    class Meta:
        model = Export
        fields = ('numexportform','dateexport','fruitexport','sizeexport','nbpalletexport')


class UpdateExportForm(forms.Form):

    fruitexport = forms.CharField(label="Fruit exporté")
    sizeexport = forms.IntegerField(label="Calibre exporté")
    nbpalletexport = forms.IntegerField(label="Nombre de palettes exportées")
    numexportform = forms.IntegerField(label="Numéro de fiche d'exportation")


class CreateFicheForm(forms.Form):
    fruitform = forms.CharField(label="Fruit exporté")
    nbfruitform = forms.IntegerField(label="Nombre de caisses")
    parcelleform = forms.CharField(label="Numéro de parcelle")
    brixform = forms.IntegerField(label="Brix")
    maturityform = forms.CharField(label="Maturité des fruits")


    class Meta:
        model = Exportform
        fields = ('fruitform', 'nbfruitform', 'parcelleform', 'brixform', 'maturityform')


class UpdateFicheForm(forms.Form):
    fruitform = forms.CharField(label="Fruit exporté")
    nbfruitform = forms.IntegerField(label="Nombre de caisses")
    parcelleform = forms.CharField(label="Numéro de parcelle")
    brixform = forms.IntegerField(label="Brix")
    maturityform = forms.CharField(label="Maturité des fruits")

