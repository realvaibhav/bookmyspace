# Generated by Django 3.2.7 on 2021-10-12 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='parking_lot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phonenumber', models.CharField(default='+91', max_length=13)),
                ('booking_price', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('opening_time', models.CharField(max_length=8)),
                ('closing_time', models.CharField(max_length=8)),
            ],
        ),
    ]