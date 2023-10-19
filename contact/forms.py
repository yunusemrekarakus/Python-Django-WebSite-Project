from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['adsoyad','email','phone','message']
        widgets = {
            'adsoyad': forms.TextInput(
                attrs={
                    'placeholder': 'AD SOYAD'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'E-MAİL'
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'placeholder': 'TELEFON NUMARASI (+905555555555)'
                }
            ),
            'message': forms.Textarea(
                attrs={
                    'placeholder': 'MESAJ'
                }
            ),
        }