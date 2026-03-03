from django import forms


class MadLibForm(forms.Form):
    place = forms.CharField(max_length=80, widget=forms.TextInput(attrs={"class": "form-control"}))
    adjective = forms.CharField(max_length=80, widget=forms.TextInput(attrs={"class": "form-control"}))
    noun = forms.CharField(max_length=80, widget=forms.TextInput(attrs={"class": "form-control"}))
    noun2 = forms.CharField(max_length=80, widget=forms.TextInput(attrs={"class": "form-control"}))
    verb = forms.CharField(max_length=80, widget=forms.TextInput(attrs={"class": "form-control"}))
    famous_person = forms.CharField(max_length=80, widget=forms.TextInput(attrs={"class": "form-control"}))
    animal = forms.CharField(max_length=80, widget=forms.TextInput(attrs={"class": "form-control"}))
