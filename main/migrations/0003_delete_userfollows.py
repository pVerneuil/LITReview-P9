# Generated by Django 4.0.3 on 2022-04-06 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_ticket_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserFollows',
        ),
    ]
