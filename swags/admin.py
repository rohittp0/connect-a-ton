from django.contrib import admin

from .models import Swag, SwagAward


@admin.register(Swag)
class SwagAdmin(admin.ModelAdmin):
    pass


@admin.register(SwagAward)
class SwagAwardAdmin(admin.ModelAdmin):
    list_filter = ('delivered',)
    list_display = ('swag', 'user', 'delivered')
    search_fields = ('swag__description', 'user__username')
