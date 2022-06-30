# Generated by Django 4.0.5 on 2022-06-30 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('BullTerrierWeb', '0007_alter_producto_imgpro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suscripcion',
            fields=[
                ('usu', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
                ('suscrito', models.BooleanField(default='False')),
            ],
        ),
        migrations.AlterField(
            model_name='producto',
            name='imgPro',
            field=models.ImageField(blank=True, null=True, upload_to='productos', verbose_name='Imagen'),
        ),
    ]
