from django import forms
from django.db.models.fields import Field
from .models import SHORTURL
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Field, Submit, Row, Field

class SHORTURLForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row (
                Column(Field("orignalurl", placeholder="Shorten You Link", css_class="form-control form-control-lg")),
                Column(Submit('submit', 'Shorten', css_class="btn btn-primary"),)
            )
        )
    class Meta:
        model = SHORTURL
        fields = ["orignalurl"]