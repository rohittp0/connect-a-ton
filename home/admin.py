from django.contrib import admin

from home.models import Question, Answer, UserConfig

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(UserConfig)
