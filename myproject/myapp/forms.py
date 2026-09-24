from django import forms
from django.utils import timezone
from .models import User, Book, Record


# User Form (Add + Edit)
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter Email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter Phone'}),
            'address': forms.Textarea(attrs={'placeholder': 'Enter Address'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        existing = User.objects.filter(email=email)
        if self.instance and self.instance.pk:
            existing = existing.exclude(pk=self.instance.pk)
        if existing.exists():
            raise forms.ValidationError('A user with this email already exists!')
        return email


# Book Form (Add + Edit)
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


# Borrow Book Form (Create Record)
class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['user', 'book', 'issue_date']

        labels = {
            'user': 'Select User',
            'book': 'Select Book',
            'issue_date': 'Issue Date'
        }

        widgets = {
            'issue_date': forms.DateInput(
                attrs={'type': 'date'}
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['issue_date'].input_formats = ['%Y-%m-%d']
        if not self.initial.get('issue_date'):
            self.initial['issue_date'] = timezone.now().date()
        open_user_ids = Record.objects.filter(status='open').values_list('user_id', flat=True)
        self.fields['user'].queryset = User.objects.exclude(id__in=open_user_ids)

class ReturnRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['return_date']
        labels = {
            'return_date': 'Return Date'
        }
        widgets = {
            'return_date': forms.DateInput(
                attrs={'type': 'date'}
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['return_date'].input_formats = ['%Y-%m-%d']