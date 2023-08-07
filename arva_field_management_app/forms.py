from django import forms
from django.forms import inlineformset_factory
from .models import Field, Client, ChannelPartner

class CSVUploadForm(forms.Form):
    csv_file = forms.FileField(label='Select a CSV file')

class FieldForm(forms.ModelForm):
    class Meta:
        model = Field
        fields = '__all__'
        exclude = ['client']
        labels = {
            'field_name': 'Field Name',
            'field_location': 'Field Location',
            'acreage': 'Acreage',
            'field_type': 'Field Type',
        }

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        exclude = ['channel_partner']
        labels = {
            'name': 'Client Name',
            'address': 'Client Address',
            'phone_number': 'Client Phone Number',
            'email': 'Client Email',
            'contact_person': 'Client Contact Person',
        }

class ChannelPartnerForm(forms.ModelForm):
    class Meta:
        model = ChannelPartner
        fields = '__all__'
        labels = {
            'name': 'Channel Partner Name',
            'address': 'Channel Partner Address',
            'phone_number': 'Channel Partner Phone Number',
            'email': 'Channel Partner Email',
        }
