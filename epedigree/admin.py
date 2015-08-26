from django.contrib import admin
from epedigree.models import UserProfile, Following, Item, Order, OrderLines, Lot, \
    Client


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('food', 'amount', 'measurement', 'recipe')

# admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(UserProfile)
admin.site.register(Following)
# Register your models here.





class FollowerInLine(admin.TabularInline):
    model = Following


class BuildingAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['custID'],
                                })

    ]
    # inlines = [JobInLine]

class OrderLinesAdmin(admin.ModelAdmin):
    list_display = ('order', 'item', 'amount', 'measurement')


admin.site.register(Client)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderLines, OrderLinesAdmin)
admin.site.register(Lot)

from django.contrib import admin
from .models import Color

admin.site.register(Color)



