# Generated by Django 3.2.4 on 2021-06-23 12:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=20, verbose_name='Mobile number')),
                ('country', models.CharField(max_length=50, verbose_name='Country')),
                ('city', models.CharField(max_length=30, verbose_name='City')),
                ('address', models.CharField(max_length=50, verbose_name='Address')),
                (
                'user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
