from django.conf import settings
from django.contrib.auth.decorators import user_passes_test

from home.models import UserConfig


def checkin_required():
    def is_checkin(user):
        if not settings.PRE_REGISTRATION:
            return True

        try:
            conf = UserConfig.objects.get(user=user)
            return conf.checked_in
        except UserConfig.DoesNotExist:
            return False

    return user_passes_test(is_checkin, login_url='checkin')
