from django import forms


class Filter(forms.Form):
    filter_fields = forms.CharField(
        label=False,
        max_length=100,
        widget=forms.Textarea,
        initial="enter your filter, example - errors:source='agent' and danger=8"
    )