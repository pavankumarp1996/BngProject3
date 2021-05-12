from django import forms


class NameForm(forms.Form):
    name = forms.CharField()
class AgeForm(forms.Form):
    Age  = forms.IntegerField()
class GfForm(forms.Form):
    Gf = forms.CharField()

