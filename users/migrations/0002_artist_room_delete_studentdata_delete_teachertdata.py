# Generated by Django 4.0.4 on 2022-04-21 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=6)),
                ('artists', models.ManyToManyField(to='users.artist')),
            ],
        ),
        migrations.DeleteModel(
            name='StudentData',
        ),
        migrations.DeleteModel(
            name='TeachertData',
        ),
    ]
