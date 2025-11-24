from django import forms
from .models import Inquiry

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['first_name', 'last_name', 'email', 'project_type', 'details']
        
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'John'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Doe'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'john@example.com'}),
            'project_type': forms.Select(attrs={'class': 'form-input', 'style': 'cursor: pointer;'}),
            'details': forms.Textarea(attrs={'class': 'form-input', 'rows': 6, 'placeholder': 'Describe your core features, target audience, and goals...'}),
        }