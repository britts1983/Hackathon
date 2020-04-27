from django import forms

class ImageUploadForm(forms.Form):
    """Image upload form."""
    pfiles = forms.FileField()
