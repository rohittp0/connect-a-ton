from django.contrib import admin

from home.models import Question, Answer, UserConfig, UserAnswer

admin.site.register(Question)


@admin.register(UserConfig)
class UserConfigAdmin(admin.ModelAdmin):
    list_filter = ('gender', 'food', 'tshirt')
    list_display = ('user', 'name', 'team', 'college', 'email')
    search_fields = ('name', 'team', 'college', 'email', 'user__username')
    readonly_fields = ('user',)
    exclude = ('other_answers', 'self_questions')

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='Registration Edit').exists():
            return 'user', 'self_questions', 'other_answers'
        elif request.user.groups.filter(name='Point Edit').exists():
            return [field.name for field in obj._meta.fields if field.name != 'points']
        return super().get_readonly_fields(request, obj)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'user', 'answer')
    search_fields = ('question__question_text', 'user__username')


@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ('answer', 'answer_value', 'question_config')
    search_fields = ('answer__question__question_text', 'question_config__user__username')
