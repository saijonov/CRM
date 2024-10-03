from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Lead, Agent, Category, FollowUp

User = get_user_model()

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'first_name',           # Shipper Information
            'last_name',
            'company_name',
            'email',
            'phone_number',
            'faxx',
            'billing_address',
            'phone_other',
            'origin_city',           # Origin & Destination
            'origin_state',
            'origin_zip_code',
            'origin_country',
            'destination_city',
            'destination_state',
            'destination_zip_code',
            'destination_country',
            'estimated_ship_date',   # Shipping Information
            'notes_from_shipper',
            'vehicle_run',
            'ship_via',
            'vehicle_year',          # Vehicle Information
            'vehicle_make',
            'vehicle_model',
            'vehicle_type',
            'vehicle_tariff',
            'vehicle_deposit',
            'total_tariff',          # Pricing Information
            'deposit'
        )

    # You can add validation for specific fields here if needed
    widgets = {
            'first_name': forms.TextInput(attrs={'class': 'border rounded-md p-2 w-full'}),
            'last_name': forms.TextInput(attrs={'class': 'border rounded-md p-2 w-full'}),
            # Add other fields similarly
        }


    def clean_first_name(self):
        data = self.cleaned_data["first_name"]
        return data

    def clean(self):
        pass


class LeadForm(forms.Form):
    # Simplified version, same as before
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}


class AssignAgentForm(forms.Form):
    agent = forms.ModelChoiceField(queryset=Agent.objects.none())

    def __init__(self, *args, **kwargs):
        request = kwargs.pop("request")
        agents = Agent.objects.filter(organisation=request.user.userprofile)
        super(AssignAgentForm, self).__init__(*args, **kwargs)
        self.fields["agent"].queryset = agents


class LeadCategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ('category',)


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)


class FollowUpModelForm(forms.ModelForm):
    class Meta:
        model = FollowUp
        fields = ('notes', 'file')
