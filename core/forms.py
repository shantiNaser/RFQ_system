from django import forms
from .models import Client, Vendor, Item, RFQ, Quotation


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['company_name', 'contact_number']


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['company_name', 'contact_number']


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description']


class RFQForm(forms.ModelForm):
    items = forms.ModelMultipleChoiceField(queryset=Item.objects.none())

    class Meta:
        model = RFQ
        fields = ['items']

    def __init__(self, client, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['items'].queryset = Item.objects.filter(client=client)


class QuotationForm(forms.ModelForm):
    class Meta:
        model = Quotation
        fields = ['estimated_cost']
