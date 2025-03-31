from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'apellido', 'correo', 'password', 'foto', 'rol']
    search_fields = ['nombre', 'apellido', 'correo']
    list_filter = ['rol']
    list_editable = ['rol']


admin.site.register(Servicio)
admin.site.register(Cita)