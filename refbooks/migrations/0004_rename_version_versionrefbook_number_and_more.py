# Generated by Django 4.1 on 2024-07-18 18:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refbooks', '0003_alter_versionrefbook_start_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='versionrefbook',
            old_name='version',
            new_name='number',
        ),
        migrations.AlterUniqueTogether(
            name='versionrefbook',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='versionrefbook',
            name='refbook',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='refbooks.refbook', verbose_name='Справочник'),
        ),
        migrations.AlterUniqueTogether(
            name='versionrefbook',
            unique_together={('refbook', 'number')},
        ),
    ]
