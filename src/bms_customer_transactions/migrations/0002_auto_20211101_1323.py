# Generated by Django 3.2.7 on 2021-11-01 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parking_lots', '0004_alter_bms_pl_booking_history_booking_date'),
        ('bms_users', '0004_auto_20211015_2103'),
        ('bms_customer_transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bms_cu_booking_history',
            name='pl_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking_lots.bms_pl_data'),
        ),
        migrations.AlterField(
            model_name='bms_cu_booking_history',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bms_users.bms_signup'),
        ),
    ]
