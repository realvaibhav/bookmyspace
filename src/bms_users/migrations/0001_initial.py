# Generated by Django 3.2.7 on 2021-10-12 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bms_signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phonenumber', models.CharField(default='+91', max_length=13)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=32)),
                ('confirm_password', models.CharField(max_length=32)),
            ],
        ),
    ]
