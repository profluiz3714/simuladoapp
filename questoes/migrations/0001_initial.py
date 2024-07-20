# Generated by Django 5.0.7 on 2024-07-20 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enunciado', models.TextField()),
                ('disciplina', models.CharField(max_length=100)),
                ('gabarito', models.CharField(max_length=1)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='imagens/')),
            ],
        ),
    ]
