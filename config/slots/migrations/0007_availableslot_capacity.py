# Generated by Django 4.2.1 on 2023-05-30 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slots', '0006_holiday_unique_holiday'),
    ]

    operations = [
        migrations.AddField(
            model_name='availableslot',
            name='capacity',
            field=models.IntegerField(default=4),
        ),
    ]