from django import forms


class SearchForm(forms.Form):
    keyword = forms.CharField(max_length=50, required=True, strip=True)