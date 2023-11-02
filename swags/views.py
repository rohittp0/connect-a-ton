from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def swags(request):
    context = {
        "swags": [
            {
                "image": "https://i.imgur.com/7k9p6lI.jpg",
                "description": "The most amazing swag of all time",
                "delivered": False,
                "unlocked": True,
                "points": None
            },
            {
                "image": "https://i.imgur.com/7k9p6lI.jpg",
                "description": "The most amazing swag of all time",
                "delivered": False,
                "unlocked": False,
                "points": 100,
            }
        ]
    }

    return render(request, 'swags/swags.html', context=context)
