# Generated by Django 3.2.7 on 2021-09-08 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210907_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesskey',
            name='access_token',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='accesskey',
            name='id_token',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
    ]
