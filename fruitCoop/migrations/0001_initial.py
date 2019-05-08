# Generated by Django 2.1.3 on 2019-05-08 12:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CreneauHoraire',
            fields=[
                ('numcreneau', models.IntegerField(primary_key=True, serialize=False)),
                ('datedebutcreneau', models.DateTimeField(verbose_name='date debut')),
                ('datefincreneau', models.DateTimeField(verbose_name='date fin')),
                ('nbpalettecreneau', models.IntegerField()),
                ('fruitcreneau', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Exportation',
            fields=[
                ('numexportation', models.IntegerField(primary_key=True, serialize=False)),
                ('nbpaletteexportation', models.IntegerField()),
                ('fruitexportation', models.CharField(max_length=20)),
                ('calibreexportation', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FicheExport',
            fields=[
                ('numfiche', models.IntegerField(primary_key=True, serialize=False)),
                ('nbfruitfiche', models.IntegerField()),
                ('fruitfiche', models.CharField(max_length=20)),
                ('brixfiche', models.IntegerField()),
                ('parcellefiche', models.CharField(max_length=10)),
                ('maturitefruitfiche', models.CharField(max_length=5)),
                ('numexportation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fruitCoop.Exportation')),
            ],
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('numlocal', models.IntegerField(primary_key=True, serialize=False)),
                ('codepostallocal', models.IntegerField()),
                ('villelocal', models.CharField(max_length=30)),
                ('adresse1local', models.CharField(max_length=40)),
                ('adresse2local', models.CharField(blank=True, max_length=40)),
                ('capacitelocal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Producteur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datenaissanceproducteur', models.DateField()),
                ('telephoneproducteur', models.CharField(max_length=15)),
                ('codepostalproducteur', models.IntegerField()),
                ('villeproducteur', models.CharField(max_length=30)),
                ('adresse1producteur', models.CharField(max_length=40)),
                ('adresse2producteur', models.CharField(blank=True, max_length=40)),
                ('numproducteur', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'producteur',
            },
        ),
        migrations.AddField(
            model_name='local',
            name='responsable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fruitCoop.Producteur'),
        ),
        migrations.AddField(
            model_name='ficheexport',
            name='numproducteur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fruitCoop.Producteur'),
        ),
    ]
