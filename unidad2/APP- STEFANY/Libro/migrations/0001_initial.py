# Generated by Django 5.1.7 on 2025-03-26 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=100)),
                ('año_publicación', models.IntegerField()),
                ('fecha_cracion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
