# Generated by Django 4.0 on 2022-03-03 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preguntas',
            name='categoria',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='respuestas',
            name='categoria',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tiempo',
            field=models.IntegerField(),
        ),
    ]
