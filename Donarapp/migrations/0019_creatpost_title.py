# Generated by Django 3.2.9 on 2022-02-02 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donarapp', '0018_creatpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='creatpost',
            name='title',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
