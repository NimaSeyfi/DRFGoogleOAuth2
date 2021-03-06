# Generated by Django 3.2.7 on 2021-09-07 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accesskey',
            name='access_token',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='accesskey',
            name='expires_in',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='accesskey',
            name='refresh_token',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='accesskey',
            name='scope',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='accesskey',
            name='token_type',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
