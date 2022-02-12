from main.models import *
from django import forms

class CandidatoCreateForm(forms.ModelForm):
    identidad = forms.CharField(required = False)
    class Meta:
        model = Candidato
        fields = [
                    'tipo',
                    'partido',
                    'identidad',
                    'nombre',
                    'Sexo',
                    'departamento',
                    'municipio',
                    #'telefono',
                    #'email',
                    #'direccion',
                    'foto',
                ]

class EscrutinioCreateForm(forms.ModelForm):
    #identidad = forms.CharField(required = False)
    class Meta:
        model = Escrutinio
        fields = [
                    'mesa',
                    'candidato',
                    'valor'
                ]
    def __init__(self, user, *args, **kwargs):
        super(EscrutinioCreateForm, self).__init__(*args, **kwargs)
        print('Al parecer sí vas al formulario')
        self.fields['centro'].queryset = CentroEducativo.objects.filter(pk =0)

class MesaCreateForm(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = [
                'centro',
                'descripcion',
                'numero'
        ]

class ColaboradorCreateForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = [
                'municipio',
                'user',
                'tipo',
                'sexo',              
                'identidad',
                'nombre',
                'foto'

        ]
# class ActaCreateForm(forms.ModelForm):
#     identidad = forms.CharField(required = False)
#     class Meta:
#         model = Acta
#         fields = [
#                     'documento',
#                     'departamento',
#                     'municipio',
#                     'aldea',
#                     'tipo',
#                     'mesa',
#                     'descripcion',
#
#                 ]
