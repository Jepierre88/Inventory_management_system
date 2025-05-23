# Generated by Django 4.2.7 on 2025-05-07 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business_management', '0003_alter_business_name'),
        ('auth_management', '0002_authuser_client_authuser_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='authuser',
            name='business',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='workers', to='business_management.business'),
        ),
    ]
