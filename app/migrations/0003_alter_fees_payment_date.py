# Generated by Django 4.0 on 2022-07-02 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_bookroom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fees',
            name='payment_date',
            field=models.DateField(null=True),
        ),
    ]
