# Generated by Django 5.0.8 on 2024-08-07 13:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('pickup_latitude', models.FloatField(blank=True, null=True)),
                ('pickup_longitude', models.FloatField(blank=True, null=True)),
                ('dropoff_latitude', models.FloatField(blank=True, null=True)),
                ('dropoff_longitude', models.FloatField(blank=True, null=True)),
                ('pickup_time', models.DateTimeField(blank=True, null=True)),
                ('datetime_inserted', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Ride',
                'verbose_name_plural': 'Rides',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('code', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='RideEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('ride', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_main.ride')),
            ],
            options={
                'verbose_name': 'Ride Event',
                'verbose_name_plural': 'Ride Events',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_main.role')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'User Profiles',
                'ordering': ['-pk'],
            },
        ),
        migrations.AddField(
            model_name='ride',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='driver', to='app_main.userprofile'),
        ),
        migrations.AddField(
            model_name='ride',
            name='rider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rider', to='app_main.userprofile'),
        ),
    ]
