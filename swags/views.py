from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def swags(request):

    context = {
        "swags": request.user.awarded_swags.all(),
    }

    return render(request, 'swags/swags.html', context=context)
