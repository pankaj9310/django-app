from django import forms

TASK_STATUS_CHOICES = ('to-do', 'Progress', 'Completed')
TASK_TYPE_CHOICES = ('Task', 'Story', 'Epic', 'Bug')
PRIORITY_CHOICES = ('Low', 'Medium', 'High')

class TaskForm(forms.Form):
    name = forms.CharField(label="Task Name", widget=forms.TextInput)
    description = forms.CharField(label="Task Description", widget=forms.Textarea)
    task_type = forms.ChoiceField(choices=TASK_TYPE_CHOICES)
    status = forms.ChoiceField(choices=TASK_STATUS_CHOICES)
    priority = forms.ChoiceField(choices=PRIORITY_CHOICES)
    due = forms.DateTimeField(label="Due Date", widget=forms.DateTimeInput)