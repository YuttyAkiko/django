from django.contrib import admin
from .models import Especialidade, Medico

# Registrando os models
admin.site.register(Especialidade)
admin.site.register(Medico)