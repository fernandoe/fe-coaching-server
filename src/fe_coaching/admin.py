from django.contrib import admin

from .models import Sessao


@admin.register(Sessao)
class SessaoModelAdmin(admin.ModelAdmin):
    list_display = ('get_uuid', 'usuario', 'entidade', 'numero', 'data', 'inicio', 'fim')
