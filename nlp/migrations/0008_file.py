# Generated by Django 4.0.4 on 2022-04-30 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nlp', '0007_cookie'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
