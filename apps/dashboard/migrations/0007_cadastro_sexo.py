# Generated by Django 2.2 on 2019-04-29 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20190429_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro',
            name='sexo',
            field=models.CharField(choices=[('----', '----'), ('MASCULINO', 'Masculino'), ('FEMININO', 'Feminino')], default='----', max_length=9, verbose_name='Qnts'),
        ),
    ]
