from django import forms


class AddForm(forms.Form):
    name = forms.CharField()
    Quntity  = forms.IntegerField()



