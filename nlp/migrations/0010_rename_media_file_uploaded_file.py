# Generated by Django 4.0.4 on 2022-04-30 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nlp', '0009_alter_file_media'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='media',
            new_name='uploaded_file',
        ),
    ]
