# Generated by Django 4.0.4 on 2022-06-21 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nlp_model', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='tweet',
            field=models.TextField(max_length=280),
        ),
    ]
