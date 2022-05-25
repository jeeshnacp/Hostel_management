# Generated by Django 4.0 on 2022-05-25 15:16

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_parent', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('complaint', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breakfast', models.CharField(max_length=50)),
                ('lunch', models.CharField(max_length=50)),
                ('dinner', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='hostel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_rooms', models.CharField(max_length=100)),
                ('occupied', models.CharField(max_length=100)),
                ('annual_expenses', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('contact_no', models.IntegerField()),
                ('room_facilities', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('age', models.IntegerField()),
                ('address', models.TextField()),
                ('contact_no', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='parent',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='parent', serialize=False, to='app.login')),
                ('role', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=40)),
                ('address', models.TextField()),
                ('child_name', models.CharField(max_length=50)),
                ('contact_no', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('approval_status', models.BooleanField(default=0)),
                ('seen', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='student', serialize=False, to='app.login')),
                ('role', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('contact_no', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('approval_status', models.BooleanField(default=0)),
                ('image', models.ImageField(null=True, upload_to='profile')),
                ('seen', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='fees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('room_rent', models.FloatField(default=0)),
                ('mess_bill', models.FloatField(default=0)),
                ('amount', models.FloatField(default=0)),
                ('status', models.BooleanField(default=False)),
                ('paid_by', models.CharField(max_length=100)),
                ('payment_date', models.DateField()),
                ('payment', models.CharField(max_length=100)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.student')),
            ],
        ),
    ]
