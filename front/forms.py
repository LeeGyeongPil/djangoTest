from django import forms
from .models import FrontBoard

class BoardRegForm(forms.ModelForm):
    class Meta:
        model = FrontBoard
        fields = ('subject','context','files',)

    def __init__(self, *args, **kwargs):
        super(BoardRegForm, self).__init__(*args, **kwargs)
        self.fields['files'].required = False

class BoardUpdateForm(forms.ModelForm):
    class Meta:
        model = FrontBoard
        fields = ('subject','context','files',)
        
    def __init__(self, *args, **kwargs):
        super(BoardUpdateForm, self).__init__(*args, **kwargs)
        self.fields['files'].required = False