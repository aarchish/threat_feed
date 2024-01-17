import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.models import User
# Create your models here.
# Table Users is auto created from django.contrib.auth.models

class Jira_Table(models.Model):
    jira_id = models.AutoField(primary_key=True)
    jira_ticket_number = models.CharField(blank=False, max_length=20)
    completed_by = models.OneToOneField(User, blank=False, on_delete=models.CASCADE)
    completed_at = models.DateTimeField("Date of completion", blank=False)

    def __str__(self):
        return self.jira_id
class ThreatFeed_Log_Table(models.Model):

    IP = "IP"
    FQDN = "FQDN"
    object_choices = {
        IP : "IP",
        FQDN : "FQDN",
    }

    Created = "Created"
    Updated = "Updated"
    Deleted = "Deleted"
    status_choices = {
        Created : "Created",
        Updated : "Updated",
        Deleted : "Deleted",
    }

    log_id = models.AutoField(primary_key=True)
    object = models.CharField(blank=False, max_length=200);
    object_type = models.CharField(choices=object_choices, default=IP, max_length=50);
    created_at = models.DateTimeField("Date of creation", blank=False)
    created_by = models.OneToOneField(User, blank=False, on_delete=models.CASCADE)
    jira_ticket_id = models.ForeignKey(Jira_Table, on_delete=models.CASCADE);
    object_status = models.CharField(choices=status_choices, default=Created, max_length=50);

class firewall_ip_objects(models.Model):
    ip_object_id = models.AutoField(primary_key=True)
    ip_object = models.GenericIPAddressField(blank=False)

class firewall_FQDN_objects(models.Model):
    FQDN_object_id = models.AutoField(primary_key=True)
    FQDN_object = models.URLField(blank=False)