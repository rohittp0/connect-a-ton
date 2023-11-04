from django.contrib import admin

from home.models import UserConfig
from .models import Swag, SwagAward


@admin.register(Swag)
class SwagAdmin(admin.ModelAdmin):
    list_display = ('description', 'points', 'stock')
    search_fields = ('description',)


@admin.register(SwagAward)
class SwagAwardAdmin(admin.ModelAdmin):
    list_filter = ('delivered',)
    list_display = ('swag', 'team', 'user', 'delivered')
    search_fields = ('swag__description', 'user__username')

    actions = ['mark_as_delivered']

    @staticmethod
    def team(obj):
        return UserConfig.objects.get(user=obj.user).team

    @staticmethod
    def mark_as_delivered(self, request, queryset):
        queryset.update(delivered=True)

    mark_as_delivered.short_description = 'Mark selected swag as delivered'
