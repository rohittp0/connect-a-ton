import random

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from home.models import UserConfig, Question, Answer, UserAnswer


@login_required
def index(request):
    # get the user's question config
    config, _ = UserConfig.objects.get_or_create(user=request.user)

    is_self = random.choice([False])

    question, answer = None, None

    if is_self:
        question = Question.objects.exclude(id__in=config.self_questions.all()).first()

    if question:
        answer, _ = Answer.objects.get_or_create(question=question, user=request.user)
    else:
        is_self = False
        answer = Answer.objects.exclude(
            Q(id__in=config.other_answers.all()) | Q(user=request.user) | Q(answer=None)).first()

    if answer is None:
        return render(request, 'home/index.html', context={"points": config.points})

    question = answer.question
    name = "your" if is_self else answer.user.first_name + " " + answer.user.last_name + "'s"

    context = {
        "question": question.question_text.replace("%USER%", name),
        "options": question.options,
        "answer": answer.id,
        "is_self": is_self,
        "points": config.points,
    }
    return render(request, 'home/index.html', context=context)


@login_required
def answer_view(request):
    if request.method != "POST":
        return redirect('home')

    answer = get_object_or_404(Answer, id=request.POST.get('answer_id'))
    answer_value = int(request.POST.get('answer'))
    is_self = answer.user == request.user

    if (answer_value < 0 or answer_value > 3) and is_self:
        return redirect('home')

    # get the user's question config
    config = get_object_or_404(UserConfig, user=request.user)

    if is_self:
        answer.answer = answer_value
        answer.save()
        config.self_questions.add(answer.question)

        return redirect('home')

    UserAnswer.objects.create(
        answer_value=answer_value,
        answer=answer,
        question_config=config,
    )

    if int(answer_value) == answer.answer:
        config.points += 5
        config.save()

    return redirect('home')
