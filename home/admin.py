from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models import Q

from home.models import Question, Answer, UserConfig, UserAnswer

admin.site.register(Question)
admin.site.unregister(User)


class CheckedInFilter(admin.SimpleListFilter):
    title = 'Checked in status'
    parameter_name = 'checked_in'

    def lookups(self, request, model_admin):
        return (
            ('1', 'Checked in'),
            ('0', 'Not Checked in'),
        )

    def queryset(self, request, queryset):
        if self.value() == '1':
            return queryset.filter(userconfig__checked_in=True)
        elif self.value() == '0':
            return queryset.filter(Q(userconfig__checked_in=False) | Q(userconfig__checked_in__isnull=True))


@admin.register(UserConfig)
class UserConfigAdmin(admin.ModelAdmin):
    list_filter = ('gender', 'food', 'tshirt', 'checked_in', 'user__is_staff')
    list_display = ('user', 'name', 'team', 'college', 'email', 'checked_in', 'points')
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
    list_display = ('answer', 'answer_value', 'question_config', 'is_correct', 'skipped')
    list_filter = ('is_correct', 'skipped')
    search_fields = ('answer__question__question_text', 'question_config__user__username')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'checked_in')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', CheckedInFilter)

    @staticmethod
    def checked_in(obj):
        try:
            return UserConfig.objects.get(user=obj).checked_in
        except UserConfig.DoesNotExist:
            return False
