# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-14 16:14
from __future__ import unicode_literals

from django.db import migrations

from awx.main.migrations import _migration_utils as migration_utils
from awx.main.migrations._multi_cred import (
    migrate_inventory_source_cred,
    migrate_inventory_source_cred_reverse
)


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_v330_create_new_rbac_roles'),
    ]

    operations = [
        # Run data migration before removing the old credential field
        migrations.RunPython(migration_utils.set_current_apps_for_migrations, migrations.RunPython.noop),
        migrations.RunPython(migrate_inventory_source_cred, migrate_inventory_source_cred_reverse),
        migrations.RemoveField(
            model_name='inventorysource',
            name='credential',
        ),
        migrations.RemoveField(
            model_name='inventoryupdate',
            name='credential',
        ),
    ]
