from django import forms

class ContatoFormAdmin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['whatsapp'].widget.attrs['class'] = 'mask-whatsapp'