# Generated by Django 2.1.3 on 2019-01-22 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0012_auto_20190122_1909'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='age_restriction',
            new_name='age_limit',
        ),
    ]
