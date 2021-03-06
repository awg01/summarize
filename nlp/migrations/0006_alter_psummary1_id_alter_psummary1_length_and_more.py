# Generated by Django 4.0.4 on 2022-04-24 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nlp', '0005_alter_psummary1_summary_alter_psummary2_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='psummary1',
            name='id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='psummary1',
            name='length',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='psummary1',
            name='summary',
            field=models.CharField(blank=True, default='', max_length=10000),
        ),
        migrations.AlterField(
            model_name='psummary2',
            name='id',
            field=models.IntegerField(default=2, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='psummary2',
            name='length',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='psummary2',
            name='summary',
            field=models.CharField(blank=True, default='', max_length=10000),
        ),
    ]
