# Generated by Django 3.2.15 on 2023-01-07 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20230105_1629'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscribe',
            options={'ordering': ('-id',), 'verbose_name': 'Subscribe', 'verbose_name_plural': 'Subscribes'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('id',), 'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
    ]
