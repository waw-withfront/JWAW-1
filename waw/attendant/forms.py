from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime  # for checking renewal date range.
from django.forms import ModelForm
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class AbsentForm(ModelForm):

    class Meta:
        model = Absent
        fields = ['student', 'absent_type', 'absent_date']


class NewAbsentForm(forms.Form):
    absent_type = forms.CharField(help_text="نوع کلاس :")
    absent_date = forms.DateField(help_text="تاریخ غیبت :")
