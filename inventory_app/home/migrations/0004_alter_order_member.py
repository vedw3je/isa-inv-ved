# Generated by Django 5.0 on 2024-01-04 19:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_member_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='member',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='member', to='home.member'),
        ),
    ]