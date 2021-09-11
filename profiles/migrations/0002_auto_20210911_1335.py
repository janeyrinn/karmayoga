# Generated by Django 3.2.6 on 2021-09-11 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='default_county',
            field=models.CharField(blank=True, default='Blank', max_length=80),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_phone_number',
            field=models.CharField(blank=True, default='blank', max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_postcode',
            field=models.CharField(blank=True, default='blank', max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_street_address1',
            field=models.CharField(blank=True, default='Blank', max_length=80),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_street_address2',
            field=models.CharField(blank=True, default='Blank', max_length=80),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_town_or_city',
            field=models.CharField(blank=True, default='Blank', max_length=40),
        ),
    ]
