# Generated by Django 2.2.2 on 2019-07-15 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('number', '0008_auto_20190715_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='Email_Address',
            field=models.EmailField(default='@gmail.com', max_length=254),
        ),
    ]
