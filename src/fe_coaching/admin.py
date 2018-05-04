from django.contrib import admin

from .models import Session


@admin.register(Session)
class SessionModelAdmin(admin.ModelAdmin):
    list_display = ('get_uuid', 'user', 'entity', 'number', 'date', 'start', 'end')
