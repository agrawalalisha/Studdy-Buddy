# Generated by Django 4.0.2 on 2022-04-26 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('studdybuddy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=100, unique=True)),
                ('user1', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='rooms1', to='studdybuddy.profile')),
                ('user2', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='rooms2', to='studdybuddy.profile')),
            ],
        ),
    ]
