from django.contrib import admin

from home.models import Question, Answer, UserConfig, UserAnswer

admin.site.register(Question)


@admin.register(UserConfig)
class UserConfigAdmin(admin.ModelAdmin):
    list_filter = ('gender', 'food', 'tshirt')
    list_display = ('name', 'team', 'college', 'email')
    search_fields = ('name', 'team', 'college', 'email', 'user__username')


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'user', 'answer')
    search_fields = ('question__question_text', 'user__username')


@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ('answer', 'answer_value')
    search_fields = ('answer__question__question_text', 'question_config__user__username')