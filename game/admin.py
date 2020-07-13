from django.contrib import admin
from .models import Player

# Register your models here.
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('user', 'power_crystals')
    list_display_links = ('user',)
    list_per_page = 10

admin.site.register(Player, PlayerAdmin)