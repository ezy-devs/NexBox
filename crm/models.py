from django.db import models
from django.utils.timezone import now
import uuid
from django.contrib.auth import get_user_model


User = get_user_model()


class Company(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='business_logos/', blank=True, null=True)
    industry = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    size = models.PositiveIntegerField(blank=True, null=True)
    annual_revenue = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    LIFECYCLE_CHOICES = [
        ('lead', 'Lead'),
        ('customer', 'Customer'),
        ('opportunity', 'Opportunity'),
        ('subscriber', 'Subscriber'),
    ]

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('archived', 'Archived'),
    ]

    LEAD_SOURCE = [
    ('website', 'Website'),
    ('referral', 'Referral'),
    ('social_media', 'Social Media'),
    ('advertisement', 'Advertisement'),
    ('email_campaign', 'Email Campaign'),
    ('event', 'Event'),
    ]

    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    job_title = models.CharField(max_length=255, blank=True, null=True)
    preferred_contact_channel = models.CharField(max_length=50, blank=True, null=True)
    preferred_contact_time = models.TimeField(blank=True, null=True)
    time_zone = models.CharField(max_length=50, blank=True, null=True)
    lifecycle_stage = models.CharField(max_length=50, choices=LIFECYCLE_CHOICES)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='active')
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE, blank=True, null=True)
    lead_source = models.CharField(max_length=50, choices=LEAD_SOURCE, blank=True, null=True)
    interests = models.TextField(blank=True, null=True)
    company = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Engagement(models.Model):
    TYPE_CHOICES = [
        ('call', 'Call'),
        ('email', 'Email'),
        ('meeting', 'Meeting'),
        ('sms', 'SMS'),
    ]

    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='engagements')
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    date_time = models.DateTimeField(default=now)
    outcome = models.CharField(max_length=255, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    automated = models.BooleanField(default=False)

    def __str__(self):
        return f"Engagement with {self.contact.first_name} {self.contact.last_name}"

class Activity(models.Model):
    ACTION_CHOICES = [
        ('website_visit', 'Website Visit'),
        ('form_submission', 'Form Submission'),
        ('email_click', 'Email Click'),
    ]

    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='activities')
    action_type = models.CharField(max_length=50, choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(default=now)
    resource = models.URLField(blank=True, null=True)
    campaign_source = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Activity: {self.action_type} for {self.contact.first_name} {self.contact.last_name}"

class Workflow(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    trigger_event = models.CharField(max_length=255)
    action_steps = models.TextField()
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('paused', 'Paused'), ('completed', 'Completed')], default='active')
    contacts = models.ManyToManyField(Contact, related_name='workflows')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Scoring(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE, related_name='scoring')
    lead_score = models.IntegerField(default=0)
    engagement_score = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Scoring for {self.contact.first_name} {self.contact.last_name}"
