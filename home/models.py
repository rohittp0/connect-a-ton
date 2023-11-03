from django.contrib.auth.models import Permission
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.conf import settings

tshirt_sizes = (
    ('xs', 'Extra Small'),
    ('s', 'Small'),
    ('m', 'Medium'),
    ('l', 'Large'),
    ('xl', 'Extra Large'),
    ('xxl', 'Double XL'),
    ('naked', 'Naked')
)

food_choices = (
    ('veg', 'Vegetarian'),
    ('non-veg', 'Non Vegetarian'),
    ('starve', 'Starve')
)

gender_choices = (
    ('male', 'Male'),
    ('female', "Female"),
    ('wm', 'Washing Machine'),
)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    options = ArrayField(models.CharField(max_length=40), size=4)

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='user')

    def __str__(self):
        return self.question.options[self.answer]


class UserAnswer(models.Model):
    answer_value = models.IntegerField()
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    question_config = models.ForeignKey('UserConfig', on_delete=models.CASCADE)


class UserConfig(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    self_questions = models.ManyToManyField(Question, related_name='self_answers')
    other_answers = models.ManyToManyField(Answer, related_name='other_answers', through='UserAnswer')

    points = models.IntegerField(default=0)
    checked_in = models.BooleanField(default=False)

    name = models.CharField(max_length=100, null=True)
    course = models.CharField(max_length=100, null=True, blank=True)
    college = models.CharField(max_length=100, null=True, blank=True)
    github = models.CharField(max_length=100, null=True, blank=True)
    tshirt = models.CharField(max_length=5, choices=tshirt_sizes, default='naked')
    year_of_study = models.IntegerField(default=-1)
    phone = models.CharField(max_length=20, null=True)
    food = models.CharField(max_length=7, choices=food_choices, default='starve')
    linkedin = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=gender_choices, default='wm')
    email = models.CharField(max_length=50, default='')
    team = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender='auth.User')
def create_model_from_csv(sender, instance, created, **kwargs):
    if not created:
        return

    data = {"email": instance.email, "name": instance.username}

    if instance.email in settings.REGISTRATION_DATA:
        data = settings.REGISTRATION_DATA[instance.email]
        data["checked_in"] = True

    UserConfig.objects.create(user=instance, **data)
