# Generated by Django 5.0.7 on 2024-07-20 02:33

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questoes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questao',
            name='enunciado',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
