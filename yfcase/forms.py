from django import forms
from django.forms import ModelForm, inlineformset_factory,Textarea 
from .models import Case,Land,Build,Personnal,Objectbuild

class CaseForm(ModelForm):
    class Meta:
        model = Case
        exclude = ()

class LandForm(ModelForm):
    class Meta:
        model = Land
        exclude = ()

class BuildForm(ModelForm):
    class Meta:
        model = Build
        exclude = ()

class PersonnalForm(ModelForm):
    class Meta:
        model = Personnal
        exclude = ()

class ObjectbuildForm(ModelForm):
    class Meta:
        model = Objectbuild
        exclude = ()

LandFormSet = inlineformset_factory(Case, Land, form=LandForm, extra=1)
BuildFormSet = inlineformset_factory(Case, Build, form=BuildForm, extra=1)
PersonnalFormSet = inlineformset_factory(Case, Personnal, form=PersonnalForm, extra=1)
ObjectbuildFormSet = inlineformset_factory(Case, Objectbuild, form=ObjectbuildForm, extra=1)

