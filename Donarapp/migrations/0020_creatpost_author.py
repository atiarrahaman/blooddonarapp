# Generated by Django 3.2.9 on 2022-07-29 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donarapp', '0019_creatpost_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='creatpost',
            name='author',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
