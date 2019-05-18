from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.core.files.storage import FileSystemStorage

storage = FileSystemStorage(location = '/')

BOOLEAN_CHOICES = (
    (True,'Oui'),
    (False,'Non'),
)

class Member(models.Model):
    nummember = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    firstnamemember = models.CharField(blank=False, max_length=50)
    lastnamemember = models.CharField(blank=False, max_length=50)
    birthdaydatemember = models.DateField()
    telephonemember = models.CharField(blank=False, max_length=15)
    postalcodemember = models.IntegerField(blank=False)
    citymember = models.CharField(blank=False, max_length=30)
    address1member = models.CharField(blank=False, max_length=40)
    address2member = models.CharField(blank=True, max_length=40)
    photomember = models.ImageField(upload_to='profile_pictures', blank=True)
    class Meta:
        db_table = 'member'


class Room(models.Model):
    numroom = models.AutoField(primary_key=True)
    nameroom = models.CharField(blank=False, max_length=30)
    postalcoderoom = models.IntegerField(blank=False)
    cityroom = models.CharField(blank=False, max_length=30)
    address1room = models.CharField(blank=False, max_length=40)
    address2room = models.CharField(blank=True, max_length=40)
    capacityroom = models.IntegerField(blank=False)
    class Meta:
        db_table = 'room'



class Exportform(models.Model):
    numform = models.AutoField(primary_key=True)
    nbfruitform = models.IntegerField(blank=False)
    fruitform = models.CharField(max_length=20)
    brixform = models.IntegerField(blank=False)
    parcelleform = models.CharField(max_length=10)
    maturityform = models.CharField(max_length=5)

    class Meta:
        db_table = 'exportform'


class Export(models.Model):
    numexport = models.AutoField(primary_key=True)
    dateexport = models.DateField('date export')
    fruitexport = models.CharField(max_length=20)
    sizeexport = models.IntegerField(blank=False)
    nbpalletexport = models.IntegerField(blank=False)
    numexportform = models.ForeignKey(Exportform, on_delete=models.CASCADE)
    class Meta:
        db_table = 'export'


class Remplir(models.Model):
    nummember = models.ForeignKey(Member, on_delete=models.CASCADE, db_column='nummember')
    numexportform = models.ForeignKey(Exportform, on_delete=models.CASCADE, db_column='numexportform')

    class Meta:
        db_table = 'remplir'
        unique_together = ('nummember', 'numexportform')

class Appartenir(models.Model):
    numroom = models.ForeignKey(Room, on_delete=models.CASCADE, db_column='numroom')
    nummember = models.ForeignKey(Member, on_delete=models.CASCADE, db_column='nummember')

    class Meta:
        db_table = 'appartenir'
        unique_together = ('numroom', 'nummember')

class Exporter(models.Model):
    numexport = models.ForeignKey(Export, on_delete=models.CASCADE, db_column='numexport')
    nummember = models.ForeignKey(Member, on_delete=models.CASCADE, db_column='nummember')

    class Meta:
        db_table = 'exporter'
        unique_together = ('numexport', 'nummember')







