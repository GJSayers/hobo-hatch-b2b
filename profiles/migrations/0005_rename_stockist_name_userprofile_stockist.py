# Generated by Django 3.2.8 on 2021-11-10 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20211110_1146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='stockist_name',
            new_name='stockist',
        ),
    ]