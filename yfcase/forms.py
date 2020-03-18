from django.forms import ModelForm, inlineformset_factory
from .models import Case,Land

class CaseForm(ModelForm):
    class Meta:
        model = Case
        exclude = ()

class LandForm(ModelForm):
    class Meta:
        model = Land
        exclude = ()

LandFormSet = inlineformset_factory(Case, Land, form=LandForm, extra=1)
