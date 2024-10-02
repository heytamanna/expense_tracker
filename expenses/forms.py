from django import forms
from .models import Expense
from django.core.exceptions import ValidationError
from django.forms.widgets import DateInput
import datetime

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['date', 'category', 'description', 'amount']
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
        }

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date > datetime.date.today():
            raise ValidationError("Date cannot be in the future.")
        return date

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount <= 0:
            raise ValidationError("Amount must be greater than zero.")
        return amount
