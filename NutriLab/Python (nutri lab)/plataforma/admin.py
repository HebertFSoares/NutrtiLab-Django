from lib2to3.pgen2.token import OP
from django.contrib import admin
from .models import Pacientes, DadosPaciente, Refeicao, Opcao

admin.site.register(Pacientes)
admin.site.register(DadosPaciente)
admin.site.register(Opcao)
admin.site.register(Refeicao)