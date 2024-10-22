# Generated by Django 5.0.7 on 2024-09-23 00:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0008_appusers_id_alter_appusers_emailaddress"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appusers",
            name="languageId",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="users",
                to="events.language",
            ),
        ),
        migrations.AlterField(
            model_name="language",
            name="languageId",
            field=models.IntegerField(max_length=1, verbose_name="language Id"),
        ),
    ]
