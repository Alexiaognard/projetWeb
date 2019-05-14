from django.db import models
from django.contrib.auth.models import User

# Create your models here.

BOOLEAN_CHOICES = (
    (True,'Oui'),
    (False,'Non'),
)

class Member(models.Model):
    nummember = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    birthdaydatemember = models.DateField()
    telephonemember = models.CharField(blank=False, max_length=15)
    postalcodemember = models.IntegerField(blank=False)
    citymember = models.CharField(blank=False, max_length=30)
    address1member = models.CharField(blank=False, max_length=40)
    address2member = models.CharField(blank=True, max_length=40)
    class Meta:
        db_table = 'member'


class Room(models.Model):
    numroom = models.IntegerField(primary_key=True)
    postalcoderoom = models.IntegerField(blank=False)
    cityroom = models.CharField(blank=False, max_length=30)
    address1room = models.CharField(blank=False, max_length=40)
    address2room = models.CharField(blank=True, max_length=40)
    capacityroom = models.IntegerField(blank=False)
    responsible = models.ForeignKey(Member, on_delete=models.CASCADE)
    class Meta:
        db_table = 'room'



class Export(models.Model):
    numexport = models.IntegerField(primary_key=True)
    dateexport = models.DateField()
    fruitexport = models.CharField(max_length=20)
    sizeexport = models.IntegerField(blank=False)
    nbpalletexport = models.IntegerField(blank=False)
    class Meta:
        db_table = 'export'


class Slot(models.Model):
    numslot = models.IntegerField(primary_key=True)
    begindateslot = models.DateTimeField('date debut')
    enddateslot = models.DateTimeField('date fin')
    nbpalletslot = models.IntegerField(blank=False)
    fruitslot = models.CharField(max_length=20)
    class Meta:
        db_table = 'slot'


class Exportform(models.Model):
    numform = models.IntegerField(primary_key=True)
    nbfruitform = models.IntegerField(blank=False)
    fruitform = models.CharField(max_length=20)
    brixform = models.IntegerField(blank=False)
    parcelleform = models.CharField(max_length=10)
    maturityform = models.CharField(max_length=5)
    numexport = models.ForeignKey(Export, on_delete=models.CASCADE)
    nummember = models.ForeignKey(Member, on_delete=models.CASCADE)

    class Meta:
        db_table = 'exportform'


class Coliser(models.Model):
    numroom = models.ForeignKey(Room, on_delete=models.CASCADE, db_column='numroom')
    numexport = models.ForeignKey(Export, on_delete=models.CASCADE, db_column='numexport')
    datecoliser = models.DateTimeField()

    class Meta:
        db_table = 'coliser'
        unique_together = ('numroom', 'numexport')

class Affecter(models.Model):
    numroom = models.ForeignKey(Room, on_delete=models.CASCADE, db_column='numroom')
    nummember = models.ForeignKey(Member, on_delete=models.CASCADE, db_column='nummember')
    isResponsible = models.BooleanField(choices=BOOLEAN_CHOICES)

    class Meta:
        db_table = 'affecter'
        unique_together = ('numroom', 'nummember')



