from django.contrib import admin
from .models import *


class GraphicInLine(admin.TabularInline):
    model = Graphic
    extra = 5


class StatInLine(admin.TabularInline):
    model = Stat
    extra = 2


class ItemAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        (None, {'fields': ['price']}),
        (None, {'fields': ['category']}),
    ]

    inlines = [StatInLine, GraphicInLine]


admin.site.register(Player)
admin.site.register(Category)
admin.site.register(Item, ItemAdmin)
admin.site.register(Stat)
admin.site.register(Graphic)