# Generated by Django 3.2.7 on 2021-09-08 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_blockedaccesskey'),
    ]

    operations = [
        migrations.CreateModel(
            name='Script',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.TextField(blank=True, max_length=5000, null=True)),
                ('language', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
    ]
