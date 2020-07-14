from django.contrib import admin
from .models import Player, Enemy

# Register your models here.
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('user', 'power_crystals', 'gold', 'hp_max', 'hp_current', 'damage')
    list_display_links = ('user',)
    list_per_page = 10


class EnemyAdmin(admin.ModelAdmin):
    list_display = ('name', 'power_crystals', 'gold', 'hp_max', 'damage')
    list_display_links = ('name',)
    list_per_page = 10

admin.site.register(Player, PlayerAdmin)
admin.site.register(Enemy, EnemyAdmin)