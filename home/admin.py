from django.contrib import admin

from home.models import Question, Answer, UserConfig, UserAnswer

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(UserConfig)
admin.site.register(UserAnswer)
