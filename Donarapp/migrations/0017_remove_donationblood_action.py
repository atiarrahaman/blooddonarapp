# Generated by Django 3.2.9 on 2022-02-02 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Donarapp', '0016_donationblood_action'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donationblood',
            name='action',
        ),
    ]