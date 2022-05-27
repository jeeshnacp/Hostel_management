# Generated by Django 4.0 on 2022-05-27 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_attendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment', models.CharField(max_length=100)),
                ('card_no', models.CharField(max_length=100)),
                ('card_cvv', models.CharField(max_length=100)),
                ('expiry_month', models.CharField(max_length=100)),
                ('expiry_year', models.CharField(max_length=100)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fee_payment', to='app.fees')),
            ],
        ),
    ]
