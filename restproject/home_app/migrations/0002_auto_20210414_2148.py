# Generated by Django 3.1.5 on 2021-04-14 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mother_tongue',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
