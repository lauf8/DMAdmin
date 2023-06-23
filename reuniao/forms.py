from django import forms
from .models import ReuniaoCastelo
from membros.models import MembroCastelo

class ReuniaoCasteloForm(forms.ModelForm):
    class Meta:
        model = ReuniaoCastelo
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(ReuniaoCasteloForm, self).__init__(*args, **kwargs)
        self.fields['data_criacao'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['membros_presentes'] = forms.MultipleChoiceField(
        choices=MembroCastelo.objects.all().values_list('id', 'nome'),
        widget=forms.CheckboxSelectMultiple)