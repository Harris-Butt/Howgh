# Generated by Django 3.2.4 on 2021-06-18 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_profile_name', models.CharField(max_length=50)),
                ('user_image', models.ImageField(null=True, upload_to='cars/')),
                ('user_profession', models.CharField(max_length=255)),
                ('user_phone_number', models.CharField(max_length=55)),
                ('user_address', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='account.account')),
            ],
        ),
    ]
