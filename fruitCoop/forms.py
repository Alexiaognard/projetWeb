from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelChoiceField
from fruitCoop.models import *


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


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'datenaissanceproducteur', 'email', 'telephoneproducteur',
                      'codepostalproducteur', 'villeproducteur', 'adresse1producteur', 'adresse2producteur','password1', 'password2')

class CreateSlotForm(forms.Form):
    begindateslot = forms.DateTimeField(label="date et heure de debut",widget=forms.SelectDateWidget(years=range(1900, 2100)))
    enddateslot = forms.DateTimeField(label="date et heure de fin",widget=forms.SelectDateWidget(years=range(1900, 2100)))
    nbpalletslot = forms.IntegerField(label="Nombre de palettes prévues")
    fruitslot = forms.CharField(label="Fruit à exporter")

    class Meta:
        model = Slot
        fields = ('begindateslot', 'enddateslot', 'nbpalletslot', 'fruitslot' )


class UpdateMemberForm(forms.Form):
    first_name = forms.CharField(label = "Prénom")
    last_name = forms.CharField(label = "Nom")
    email = forms.EmailField(label = "Adresse électronique")
    datenaissanceproducteur = forms.DateField(label="Date de naissance",widget=forms.SelectDateWidget(years=range(1900, 2100)))
    telephoneproducteur = forms.CharField(label="Numéro de téléphone")
    codepostalproducteur = forms.IntegerField(label="Code postal")
    villeproducteur = forms.CharField(label="Ville")
    adresse1producteur = forms.CharField(label="Adresse1")
    adresse2producteur = forms.CharField(label="Adresse2")

class addRoomForm(forms.Form):
    choice_room = RoomChoiceField(queryset=Room.objects.all(), to_field_name='nameroom', label="Local")


