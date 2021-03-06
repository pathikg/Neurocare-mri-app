from dataclasses import fields
from email import message
from django import forms

from segmi.models import appointment, lab_report

class ReportForm(forms.ModelForm):
	class Meta:
		model = lab_report
		fields = ['lab','patient','doctor','report_summary','medicines','Mark_as_seen']

class LabReportsegmentForm(forms.ModelForm):
	
    class Meta:
        model = lab_report
        fields = ['segment_img']


class LabReportForm(forms.ModelForm):
	
    class Meta:
        model = lab_report
        fields = ['lab','patient','doctor','report_img','report_summary']


class AppointmentForm(forms.ModelForm):
	
    class Meta:
        model = appointment
        fields = ['date','department','doctor','message']
        widgets = {
            'date': forms.widgets.DateInput(attrs={'type': 'date'})
        }

class Apform(forms.ModelForm):
    class Meta:
        model = appointment
        fields ='__all__'
        