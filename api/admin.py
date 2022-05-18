from django.contrib import admin
from .models import *


class GraphicInLine(admin.TabularInline):
    model = Graphic
    extra = 5


class ItemAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        (None, {'fields': ['price']}),
        (None, {'fields': ['category']}),
    ]

    inlines = [GraphicInLine]


admin.site.register(Player)
admin.site.register(Category)
admin.site.register(Item, ItemAdmin)
admin.site.register(Graphic)