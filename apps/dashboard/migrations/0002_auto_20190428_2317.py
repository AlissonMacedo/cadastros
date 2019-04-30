# Generated by Django 2.2 on 2019-04-29 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro',
            name='estadocivil',
            field=models.CharField(choices=[('SOLTEIRO(A)', 'Solteiro(a)'), ('CASADO(A)', 'Casado(a)')], default='-----', max_length=9),
        ),
        migrations.AddField(
            model_name='cadastro',
            name='filhos',
            field=models.CharField(choices=[('NÃO', 'Não'), ('1', '1'), ('2', '2'), ('3', '3'), ('4 OU MAIS', '4 ou mais')], default='NÃO', max_length=9),
        ),
    ]