from django.contrib import admin
from .models import Zadanie

@admin.register(Zadanie)
class ZadanieAdmin(admin.ModelAdmin):
    list_display = ("tytul", "status", "priorytet", "termin", "utworzono")
    list_filter = ("status", "priorytet")
    search_fields = ("tytul", "opis")
