from django.forms import ModelForm
from .models import *

class Add_contactForm(ModelForm):
    class Meta:
        model = Contact_book
        fields = ("__all__")

    def __init__(self, *args, **kwargs):
        super(Add_contactForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class':'form-control'})