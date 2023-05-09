from django import forms


class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    email = forms.CharField(max_length=60, required=True)
    subject = forms.CharField(max_length=60, required=False)
    message = forms.CharField(widget=forms.Textarea(
        attrs={"rows": 5}
    ), required=True)
