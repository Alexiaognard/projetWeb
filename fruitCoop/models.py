from django.db import models
from django.contrib.auth.models import User

# Create your models here.

BOOLEAN_CHOICES = (
    (True,'Oui'),
    (False,'Non'),
)

class Producteur(models.Model):
    numproducteur = models.OneToOneField(User, on_delete=models.CASCADE)
    datenaissanceproducteur = models.DateField()
    telephoneproducteur = models.CharField(blank=False, max_length=15)
    codepostalproducteur = models.IntegerField(blank=False)
    villeproducteur = models.CharField(blank=False, max_length=30)
    adresse1producteur = models.CharField(blank=False, max_length=40)
    adresse2producteur = models.CharField(blank=True, max_length=40)
    class Meta:
        db_table = 'producteur'


class Local(models.Model):
    numlocal = models.IntegerField(primary_key=True)
    codepostallocal = models.IntegerField(blank=False)
    villelocal = models.CharField(blank=False, max_length=30)
    adresse1local = models.CharField(blank=False, max_length=40)
    adresse2local = models.CharField(blank=True, max_length=40)
    capacitelocal = models.IntegerField(blank=False)
    responsable = models.ForeignKey(Producteur, on_delete=models.CASCADE)
    class Meta:
        db_table = 'local'



class Exportation(models.Model):
    numexportation = models.IntegerField(primary_key=True)
    nbpaletteexportation = models.IntegerField(blank=False)
    fruitexportation = models.CharField(max_length=20)
    calibreexportation = models.IntegerField(blank=False)
    class Meta:
        db_table = 'exportation'


class CreneauHoraire(models.Model):
    numcreneau = models.IntegerField(primary_key=True)
    datedebutcreneau = models.DateTimeField('date debut')
    datefincreneau = models.DateTimeField('date fin')
    nbpalettecreneau = models.IntegerField(blank=False)
    fruitcreneau = models.CharField(max_length=20)
    class Meta:
        db_table = 'creneau'



class FicheExport(models.Model):
    numfiche = models.IntegerField(primary_key=True)
    nbfruitfiche = models.IntegerField(blank=False)
    fruitfiche = models.CharField(max_length=20)
    brixfiche = models.IntegerField(blank=False)
    parcellefiche = models.CharField(max_length=10)
    maturitefruitfiche = models.CharField(max_length=5)
    numexportation = models.ForeignKey(Exportation, on_delete=models.CASCADE)
    numproducteur = models.ForeignKey(Producteur, on_delete=models.CASCADE)

    class Meta:
        db_table = 'fiche'


class Coliser(models.Model):
    numlocal = models.ForeignKey(Local, on_delete=models.CASCADE, db_column='numlocal')
    numexportation = models.ForeignKey(Exportation, on_delete=models.CASCADE, db_column='numexportation')
    datecoliser = models.DateTimeField()

    class Meta:
        db_table = 'coliser'
        unique_together = ('numlocal', 'numexportation')

class Affecter(models.Model):
    numlocal = models.ForeignKey(Local, on_delete=models.CASCADE, db_column='numlocal')
    numproducteur = models.ForeignKey(Exportation, on_delete=models.CASCADE, db_column='numproducteur')
    isResponsable = models.BooleanField(choices=BOOLEAN_CHOICES)

    class Meta:
        db_table = 'affecter'
        unique_together = ('numlocal', 'numproducteur')


