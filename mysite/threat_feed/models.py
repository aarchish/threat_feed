import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.models import User
# Create your models here.
# Table Users is auto created from django.contrib.auth.models

class ThreatFeed_Log_Table(models.Model):
    log_id = models.AutoField(primary_key=True)
    object = models.CharField(blank=False);
    object_type = models.CharField(blank=False)
    created_at = models.DateTimeField("Date of creation",blank=False)
    created_by = models.OneToOneField(User, blank=False, on_delete=models.CASCADE)
    jira_ticket = models.CharField(blank=False);
    object_status = models.CharField(blank=False);

class Jira_Table(models.Model):
    jira_id = models.AutoField(primary_key=True)
    jira_ticket_number = models.ForeignKey(ThreatFeed_Log_Table, blank=False, on_delete=models.CASCADE)
    completed_by = models.OneToOneField(User, blank=False, on_delete=models.CASCADE)
    completed_at = models.DateTimeField("Date of completion")

class firewall_ip_objects(models.Model):
    ip_object_id = models.AutoField(primary_key=True)
    ip_object = models.CharField(blank=False)

class firewall_FQDN_objects(models.Model)
    FQDN_object_id = models.AutoField(primary_key=True)
    FQDN_object = models.CharField(blank=False)