# Generated by Django 4.2.1 on 2023-07-08 08:39

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailingClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='ФИО')),
                ('contact_email', models.EmailField(max_length=254, unique=True, verbose_name='контактный email')),
                ('comment', models.CharField(blank=True, max_length=255, null=True, verbose_name='комментарий')),
            ],
            options={
                'verbose_name': 'Клиент для рассылки',
                'verbose_name_plural': 'Клиенты для рассылки',
            },
        ),
        migrations.CreateModel(
            name='StatusType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('full_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='ФИО')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='контактный email')),
                ('comment', models.CharField(blank=True, max_length=255, null=True, verbose_name='комментарий')),
                ('is_active', models.BooleanField(default=False, verbose_name='активный')),
                ('status_type', models.CharField(choices=[('MANAGER', 'Manager'), ('BASE_USER', 'Base_user'), ('CONTENT_MANAGER', 'Content_manager')], default='BASE_USER', max_length=50, verbose_name='роль')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]