from django import forms

from .models import Fundraiser, Pledge


class PledgeForm(forms.ModelForm):
    class Meta:
        model = Pledge
        fields = ["name", "phone", "amount"]

    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        if not phone.isdigit() or len(phone) != 10 or not phone.startswith("0"):
            raise forms.ValidationError("Use 10 digits starting with 0, like 0712345678.")
        return phone

    def clean_amount(self):
        amount = self.cleaned_data["amount"]
        if amount < 1000:
            raise forms.ValidationError("The smallest pledge is TZS 1,000.")
        return amount


class FundraiserForm(forms.ModelForm):
    class Meta:
        model = Fundraiser
        fields = ["name", "description", "target"]
