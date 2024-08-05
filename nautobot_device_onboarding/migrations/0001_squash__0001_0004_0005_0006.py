# Generated by Django 3.2.21 on 2023-10-13 16:17

import uuid

import django.db.models.deletion
from django.db import migrations, models
from nautobot.extras.models import RoleField


class Migration(migrations.Migration):
    initial = True

    replaces = [
        ("nautobot_device_onboarding", "0001_initial"),
        ("nautobot_device_onboarding", "0004_migrate_to_extras_role_part_1"),
        ("nautobot_device_onboarding", "0004_migrate_to_extras_role_part_2"),
        ("nautobot_device_onboarding", "0004_migrate_to_extras_role_part_3"),
        ("nautobot_device_onboarding", "0005_migrate_site_to_location_part_1"),
        ("nautobot_device_onboarding", "0005_migrate_site_to_location_part_2"),
        ("nautobot_device_onboarding", "0005_migrate_site_to_location_part_3"),
        ("nautobot_device_onboarding", "0006_update_model_fields_part_1"),
        ("nautobot_device_onboarding", "0006_update_model_fields_part_2"),
        ("nautobot_device_onboarding", "0006_update_model_fields_part_3"),
    ]

    dependencies = [
        ("dcim", "0049_remove_slugs_and_change_device_primary_ip_fields"),
        ("extras", "0098_rename_data_jobresult_result"),
    ]

    operations = [
        migrations.CreateModel(
            name="OnboardingDevice",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("enabled", models.BooleanField(default=True)),
                ("device", models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to="dcim.device")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="OnboardingTask",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                ("ip_address", models.CharField(max_length=255)),
                ("device_type", models.CharField(blank=True, default="", max_length=255)),
                ("status", models.CharField(blank=True, default="", max_length=255)),
                ("failed_reason", models.CharField(blank=True, default="", max_length=255)),
                ("message", models.CharField(blank=True, max_length=511)),
                ("port", models.PositiveSmallIntegerField(default=22)),
                ("timeout", models.PositiveSmallIntegerField(default=30)),
                (
                    "created_device",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="dcim.device"
                    ),
                ),
                (
                    "location",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="dcim.location"
                    ),
                ),
                (
                    "platform",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="dcim.platform"
                    ),
                ),
                (
                    "role",
                    RoleField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="onboarding_tasks",
                        to="extras.role",
                    ),
                ),
            ],
        ),
    ]
