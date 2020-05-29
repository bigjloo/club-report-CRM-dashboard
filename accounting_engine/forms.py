from django import forms
import datetime


class DateForm(forms.Form):
    start_date = forms.DateField(
        widget=forms.SelectDateWidget(), initial=datetime.date.today, )
    end_date = forms.DateField(
        widget=forms.SelectDateWidget(), initial=datetime.date.today, )


class CPForm(forms.Form):
    cparea = forms.CharField(widget=forms.Textarea, label="Copy Paste REPORT")
