# Generated by Django 4.1.3 on 2022-11-18 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='numero_dia',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
