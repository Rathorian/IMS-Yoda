# Generated by Django 5.0.7 on 2024-08-04 14:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=128, unique=True, verbose_name='Adresse e-mail')),
                ('first_name', models.CharField(max_length=64, verbose_name='Prénom')),
                ('last_name', models.CharField(max_length=64, verbose_name='Nom')),
                ('password', models.CharField(max_length=128, verbose_name='Mot de passe')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='Date de la dernière connexion')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name="Date d'inscription")),
                ('is_active', models.BooleanField(default=True, verbose_name="Status d'activation")),
                ('is_staff', models.BooleanField(default=False, verbose_name='Staff')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Administrateur')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Utilisateur',
                'verbose_name_plural': 'Utilisateurs',
            },
        ),
    ]
