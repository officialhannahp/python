# Generated by Django 2.2.4 on 2021-03-22 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default=()),
            preserve_default=False,
        ),
    ]
