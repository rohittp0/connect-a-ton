from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def index(request):
    context = {
        "question": 'What is the meaning of life, the universe, and everything?',
        "options": [
            (0, "GJI"),
            (1, "Make a Ton"),
            (2, "42"),
            (3, "I don't know")
        ]
    }
    return render(request, 'home/index.html', context=context)
