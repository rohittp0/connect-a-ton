from django.contrib.postgres.fields import ArrayField
from django.db import models


# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    options = ArrayField(models.CharField(max_length=40), size=4)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_value = models.IntegerField()
    actual_answer = models.IntegerField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)


class QuestionConfig(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    self_questions = models.ManyToManyField(Question, related_name='self_answers')
    other_answers = models.ManyToManyField(Answer, related_name='other_answers')

    points = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
