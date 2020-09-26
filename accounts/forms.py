from django import forms
from accounts.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nome', 'cpf', 'dataNascimento', 'email', 'senha', 'telefone', 'isProdutor']
