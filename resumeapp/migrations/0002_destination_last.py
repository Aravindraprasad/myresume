# Generated by Django 4.1.5 on 2023-01-05 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='last',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
