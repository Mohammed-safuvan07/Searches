
from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Search for countries or capitals...'}))
