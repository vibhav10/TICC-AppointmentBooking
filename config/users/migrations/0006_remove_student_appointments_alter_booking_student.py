# Generated by Django 4.2.1 on 2023-06-02 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_booking_additional_info_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='appointments',
        ),
        migrations.AlterField(
            model_name='booking',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='users.student'),
        ),
    ]
