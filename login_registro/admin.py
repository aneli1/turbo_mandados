from django.contrib import admin
from .models import Usuario

# usuarios/admin.py
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'correo','password')
    search_fields = ('nombre', 'apellidos', 'correo')
    list_filter = ('correo',)

admin.site.register(Usuario, UsuarioAdmin)