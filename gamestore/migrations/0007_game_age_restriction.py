# Generated by Django 2.1.3 on 2019-01-22 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0006_auto_20190122_0306'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='age_restriction',
            field=models.PositiveIntegerField(default=2),
            preserve_default=False,
        ),
    ]
