# Generated by Django 4.2.5 on 2023-10-03 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentmanagement', '0002_remove_payment_amount_paid_remove_rental_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rental',
            name='no_of_rooms',
        ),
    ]
