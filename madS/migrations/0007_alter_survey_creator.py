# Generated by Django 5.1.7 on 2025-03-16 00:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madS', '0006_alter_response_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='surveys', to='madS.customuser'),
        ),
    ]
