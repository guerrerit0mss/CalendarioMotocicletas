# Generated by Django 4.0 on 2022-03-03 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trivias', '0002_alter_preguntas_categoria_alter_respuestas_categoria_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='respuestas',
            old_name='categoria',
            new_name='pregunta',
        ),
    ]