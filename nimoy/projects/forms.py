from django import forms

PROJECT_TYPE_CHOICES = (
	   ('software', 'Software'),
	   ('business', 'Business'),)

class ProjectForm(forms.Form):
    name = forms.CharField(label="Project Name", widget=forms.TextInput)
    description = forms.CharField(label="Project Description", widget=forms.Textarea)
    project_type = forms.ChoiceField(choices=PROJECT_TYPE_CHOICES)
