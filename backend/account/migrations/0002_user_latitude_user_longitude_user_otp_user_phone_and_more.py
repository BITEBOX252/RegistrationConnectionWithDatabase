# Generated by Django 5.0.8 on 2024-09-28 06:57

import django.db.models.deletion
import shortuuid.django_fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='otp',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, default='profile/default.jpg', null=True, upload_to='profile/')),
                ('full_name', models.CharField(blank=True, max_length=50, null=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.CharField(blank=True, max_length=150, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('pid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijk', length=10, max_length=20, prefix='', unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
