# Generated by Django 3.0.3 on 2020-07-31 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothessite', '0004_delete_signupmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('conf_num', models.CharField(max_length=15)),
                ('confirmed', models.BooleanField(default=False)),
            ],
        ),
    ]
