from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(required=True)
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
