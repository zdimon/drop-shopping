# Generated by Django 3.0.5 on 2020-06-12 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0005_auto_20200515_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.CharField(default='', max_length=250),
        ),
    ]