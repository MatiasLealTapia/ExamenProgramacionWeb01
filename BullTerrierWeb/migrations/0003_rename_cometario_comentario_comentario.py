# Generated by Django 4.0.5 on 2022-06-09 00:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BullTerrierWeb', '0002_remove_comentario_nota_comentario_calificacion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='cometario',
            new_name='comentario',
        ),
    ]
