# Generated by Django 2.2 on 2019-04-29 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20190429_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='datadenascimento',
            field=models.DateTimeField(max_length=10, verbose_name='Data Nascimento'),
        ),
    ]
