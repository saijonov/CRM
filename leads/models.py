from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_organisor = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class LeadManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


class Lead(models.Model):
    # Shipper Information
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    phone_other = models.CharField(max_length=20, null=True, blank=True)
    faxx = models.CharField(max_length=20, null=True, blank=True)
    billing_address = models.TextField(null=True, blank=True)

    # Origin & Destination Information
    origin_zip_code = models.CharField(max_length=10, blank=True)  # Origin zip code field
    origin_city = models.CharField(max_length=100, blank=True)      # Origin city field
    origin_state = models.CharField(max_length=100, blank=True)     # Origin state field
    origin_country = models.CharField(max_length=100, blank=True)     # Origin state field

    destination_zip_code = models.CharField(max_length=10, blank=True)  # Destination zip code field
    destination_city = models.CharField(max_length=100, blank=True)      # Destination city field
    destination_state = models.CharField(max_length=100, blank=True)  # Or another default value
    destination_country = models.CharField(max_length=100, blank=True) 


    # Shipping Information
    estimated_ship_date = models.DateField(null=True, blank=True)
    notes_from_shipper = models.TextField(null=True, blank=True)
    vehicle_run = models.BooleanField(default=False)
    ship_via = models.CharField(max_length=50, null=True, blank=True)

    # Vehicle Information
    vehicle_year = models.CharField(max_length=4, blank=True)
    vehicle_make = models.CharField(max_length=50, blank=True)
    vehicle_model = models.CharField(max_length=50, blank=True)
    vehicle_type = models.CharField(max_length=50, blank=True)
    vehicle_tariff = models.CharField(max_length=50, blank=True)
    vehicle_deposit = models.CharField(max_length=50, blank=True)


    # Pricing Information
    total_tariff = models.CharField(max_length=50, blank=True)
    deposit = models.CharField(max_length=50, blank=True)

    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    agent = models.ForeignKey("Agent", null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey("Category", related_name="leads", null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    converted_date = models.DateTimeField(null=True, blank=True)

    objects = LeadManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

    order_id = models.IntegerField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.order_id is None:
            # Get the last order ID from the database, if any
            last_order = Lead.objects.order_by('order_id').last()
            if last_order:
                self.order_id = last_order.order_id + 1
            else:
                self.order_id = 10400001  # Starting order ID
        
        super().save(*args, **kwargs)





def handle_upload_follow_ups(instance, filename):
    return f"lead_followups/lead_{instance.lead.pk}/{filename}"


class FollowUp(models.Model):
    lead = models.ForeignKey(Lead, related_name="followups", on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)
    file = models.FileField(null=True, blank=True, upload_to=handle_upload_follow_ups)

    def __str__(self):
        return f"{self.lead.first_name} {self.lead.last_name}"


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


class Category(models.Model):
    name = models.CharField(max_length=30)  # New, Contacted, Converted, Unconverted
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(post_user_created_signal, sender=User)
