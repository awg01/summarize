# Generated by Django 4.0.4 on 2022-04-24 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nlp', '0002_rename_psummaryform2_psummary1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='psummary1',
            name='length',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='psummary2',
            name='length',
            field=models.IntegerField(default=1),
        ),
    ]
