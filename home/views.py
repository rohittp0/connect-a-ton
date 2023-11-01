import random

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from home.models import UserConfig, Question, Answer, UserAnswer


@login_required
def index(request):
    # get the user's question config
    config, _ = UserConfig.objects.get_or_create(user=request.user)

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


@login_required
def answer_view(request):
    if request.method != "POST":
        return redirect('home')

    answer = get_object_or_404(Answer, id=request.POST.get('answer_id'))
    answer_value = request.POST.get('answer')
    is_self = answer.user == request.user

    if not answer_value:
        return redirect('home')

    if is_self:
        answer.actual_answer = answer_value
        answer.save()
        return redirect('home')

    # get the user's question config
    config = get_object_or_404(UserConfig, user=request.user)

    UserAnswer.objects.create(
        answer_value=answer_value,
        answer=answer,
        question_config=config,
    )

    if int(answer_value) == answer.actual_answer:
        config.points += 1
        config.save()

    return redirect('home')

