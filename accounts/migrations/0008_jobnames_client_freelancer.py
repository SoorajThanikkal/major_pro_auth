# Generated by Django 5.0 on 2023-12-28 17:20

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_user_is_client_remove_user_is_freelancer'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobNames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobcategory', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profilepic', models.ImageField(blank=True, null=True, upload_to='profile_photos')),
                ('phone', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator(message='Phone number must be a 10-digit number.', regex='^\\d{10}$')])),
                ('address', models.CharField(default='', max_length=50)),
                ('about', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='client', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Freelancer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profilepic', models.ImageField(blank=True, null=True, upload_to='profile_photos')),
                ('phone', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator(message='Phone number must be a 10-digit number.', regex='^\\d{10}$')])),
                ('address', models.CharField(default='', max_length=250)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('experiance', models.CharField(choices=[('Entry Level', 'Entry Level'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], default='Entry Level', max_length=20)),
                ('age', models.PositiveIntegerField(default=0)),
                ('about', models.TextField(default='')),
                ('price', models.PositiveIntegerField(default=0)),
                ('portfolio', models.URLField(blank=True, null=True)),
                ('availability', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='freelancer', to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.jobnames')),
            ],
        ),
    ]