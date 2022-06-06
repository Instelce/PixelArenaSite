from django.contrib import admin
from .models import *


class GraphicInLine(admin.TabularInline):
    model = Graphic
    extra = 5


class ItemStatInLine(admin.TabularInline):
    model = ItemStat
    extra = 2


class PlayerItemInLine(admin.TabularInline):
    model = PlayerItem
    extra = 0


class PlayerAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ['user']}),
        (None, {"fields": ['coins']}),
    )

    inlines = [PlayerItemInLine]
    

class ItemAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        (None, {'fields': ['price']}),
        (None, {'fields': ['category']}),
    ]

    inlines = [ItemStatInLine, GraphicInLine]


admin.site.register(Player, PlayerAdmin)
admin.site.register(Category)
# Items
admin.site.register(Item, ItemAdmin)
admin.site.register(PlayerItem)
# Items Stats
admin.site.register(ItemStat)

admin.site.register(Graphic)