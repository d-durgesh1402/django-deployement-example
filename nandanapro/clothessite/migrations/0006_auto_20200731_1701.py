# Generated by Django 3.0.3 on 2020-07-31 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothessite', '0005_subscriber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='email',
            field=models.EmailField(default=False, max_length=254),
        ),
    ]