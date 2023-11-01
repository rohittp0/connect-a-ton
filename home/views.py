import random

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from home.models import QuestionConfig, Question, Answer


@login_required
def index(request):
    # get the user's question config
    config, _ = QuestionConfig.objects.get_or_create(user=request.user)

    is_self = random.choice([True])

    question, answer = None, None

    if is_self:
        question = Question.objects.exclude(id__in=config.self_questions.all()).first()

    if question:
        answer, _ = Answer.objects.get_or_create(question=question, user=request.user, actual_answer=-8,
                                                 answer_value=-1)
    else:
        is_self = False
        answer = Answer.objects.exclude(id__in=config.other_answers.all()).exclude(user=request.user).first()

    if answer is None:
        return render(request, 'home/index.html')

    question = answer.question
    name = "your" if is_self else answer.user.username

    context = {
        "question": question.question_text.replace("%USER%", name),
        "options": question.options,
        "answer": answer.id,
        "is_self": is_self,
    }
    return render(request, 'home/index.html', context=context)
