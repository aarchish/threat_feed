# Generated by Django 5.0.1 on 2024-01-17 15:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='firewall_FQDN_objects',
            fields=[
                ('FQDN_object_id', models.AutoField(primary_key=True, serialize=False)),
                ('FQDN_object', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='firewall_ip_objects',
            fields=[
                ('ip_object_id', models.AutoField(primary_key=True, serialize=False)),
                ('ip_object', models.GenericIPAddressField()),
            ],
        ),
        migrations.CreateModel(
            name='Jira_Table',
            fields=[
                ('jira_id', models.AutoField(primary_key=True, serialize=False)),
                ('jira_ticket_number', models.CharField(max_length=20)),
                ('completed_at', models.DateTimeField(verbose_name='Date of completion')),
                ('completed_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ThreatFeed_Log_Table',
            fields=[
                ('log_id', models.AutoField(primary_key=True, serialize=False)),
                ('object', models.CharField(max_length=200)),
                ('object_type', models.CharField(choices=[('IP', 'IP'), ('FQDN', 'FQDN')], default='IP', max_length=50)),
                ('created_at', models.DateTimeField(verbose_name='Date of creation')),
                ('object_status', models.CharField(choices=[('Created', 'Created'), ('Updated', 'Updated'), ('Deleted', 'Deleted')], default='Created', max_length=50)),
                ('created_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('jira_ticket_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='threat_feed.jira_table')),
            ],
        ),
    ]