# Generated by Django 5.0.6 on 2024-05-18 20:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_participant_module_participant_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='module',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.module'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.task'),
        ),
        migrations.AlterField(
            model_name='task',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='main.module'),
        ),
    ]