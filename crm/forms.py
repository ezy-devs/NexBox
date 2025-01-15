from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = [
            'first_name', 'middle_name', 'last_name', 'email', 'phone_number',
            'company', 'job_title', 'preferred_contact_channel', 'preferred_contact_time', 'lifecycle_stage','status', 'tags', 'lead_source', 'interests', 'address', 'city', 'state', 'zipcode', 'country'
        ]
        labels = {
            'first_name': 'First Name',
            'middle_name': 'Middle Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'phone_number': 'Phone Number',
            'company': 'Company',
            'job_title': 'Job Title',
            'preferred_contact_channel': 'Preferred Contact Channel',
            'preferred_contact_time': 'Preferred Contact Time',
            'lifecycle_stage': 'Lifecycle Stage',
            'status': 'Status',
            'tags': 'Tags',
            'lead_source': 'Lead Source',
            'interests': 'Interests',
            'address': 'Address',
            'city': 'City',
            'state': 'State',
            'zipcode': 'Zipcode',
            'country': 'Country',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'zipcode': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'job_title': forms.TextInput(attrs={'class': 'form-control'}),
            'preferred_contact_channel': forms.TextInput(attrs={'class': 'form-control'}),
            'preferred_contact_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'lifecycle_stage': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.Select(attrs={'class': 'form-control'}),
            'lead_source': forms.Select(attrs={'class': 'form-control'}),
            'interests': forms.Textarea(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
        }

