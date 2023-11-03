from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from connect_a_ton.utils import checkin_required
from home.models import UserConfig
from swags.models import Swag, SwagAward


@login_required
@checkin_required()
def swags(request):
    config = get_object_or_404(UserConfig, user=request.user)
    unlocked_swags = request.user.awarded_swags.all()

    # Unlock locked swags if user has enough points
    unlockable_swags = Swag.objects.filter(points__lte=config.points).filter(stock__gt=0).exclude(pk__in=unlocked_swags)

    for swag in unlockable_swags:
        SwagAward.objects.create(user=request.user, swag=swag)

    unlocked_swags = request.user.awarded_swags.all().order_by('points')
    locked_swags = Swag.objects.exclude(pk__in=unlocked_swags).order_by('points')

    context = {
        "swag_types": ((unlocked_swags, "unlocked"), (locked_swags, "locked")),
    }

    return render(request, 'swags/swags.html', context=context)
