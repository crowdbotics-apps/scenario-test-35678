# Bad example for a data migration
from django.db import migrations
from django.core.management import call_command


def load_fixture(apps, schema_editor):
    # No, it's wrong. DON'T DO THIS!
    call_command('loaddata', 'plan.json', app_label='plans')


class Migration(migrations.Migration):
    dependencies = [
        # Dependencies to other migrations
    ]

    operations = [
        migrations.RunPython(load_fixture),
    ]
