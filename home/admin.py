from django.contrib import admin

from home.models import Question, Answer, QuestionConfig

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(QuestionConfig)
