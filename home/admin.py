from django.contrib import admin

from home.models import Question, Answer, UserConfig, UserAnswer

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(UserAnswer)


@admin.register(UserConfig)
class UserConfigAdmin(admin.ModelAdmin):
    list_filter = ('gender', 'food', 'tshirt')
    list_display = ('name', 'team', 'college', 'email')
    search_fields = ('name', 'team', 'college', 'email', 'user__username')
