# Generated by Django 3.2.9 on 2021-12-03 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donarapp', '0006_auto_20211203_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='alldonar',
            name='address',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='alldonar',
            name='age',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='alldonar',
            name='district',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='alldonar',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='alldonar',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='alldonar',
            name='last_donate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='alldonar',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]