from django import forms
from . models import *

class PSummaryForm1(forms.ModelForm):
    class Meta:
        model = PSummary1
        fields = ["paragraph", "length", "summary"]
        widgets = {'summary': forms.HiddenInput()}


    # paragraph = forms.CharField(label='Paragraph to summarize', max_length=10000)
    # length = forms.IntegerField(label='Number of sentences', required=False)
    # # summary = forms.CharField(label='summary',  max_length=10000, required=False)

class PSummaryForm2(forms.ModelForm):
    class Meta:
        model = PSummary2
        fields = ["paragraph", "length", "summary"]
        widgets = {'summary': forms.HiddenInput()}

    # paragraph = forms.CharField(label='Paragraph to summarize', max_length=10000)
    # length = forms.IntegerField(label='Number of sentences', required=False)
    # summary = forms.CharField(label='summary',  max_length=10000, required=False)

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields= ["uploaded_file", "file_contents", "summary_of_file_contents", "length"]
        widgets = {'file_contents': forms.HiddenInput(), 'summary_of_file_contents': forms.HiddenInput()}

        # uploaded_file = models.FileField(upload_to="media", null=True, blank=True)
        # file_contents = models.CharField(max_length=10000, default="", blank=True)
        # summary_of_file_contents = models.CharField(max_length=10000, default="", blank=True)

class DisplayFileForm(forms.ModelForm):
    class Meta:
        model = DisplayFile
        fields= '__all__'
