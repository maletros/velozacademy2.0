# Generated by Django 5.0.6 on 2025-03-28 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0004_aula_video_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='desconto',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='preco',
        ),
    ]
