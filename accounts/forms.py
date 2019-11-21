from django import forms
from accounts.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
<<<<<<< HEAD
        fields = ['nome', 'cpf', 'dataNascimento', 'email', 'senha', 'telefone', 'isProdutor']
=======
        fields = ['nome', 'cpf', 'dataNascimento', 'email', 'senha', 'telefone']
>>>>>>> 2de61abb52edc5456bba7a7913595b33133d95c9
