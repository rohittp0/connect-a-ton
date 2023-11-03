from django.contrib.auth.decorators import user_passes_test

from home.models import UserConfig


def checkin_required():
    def is_checkin(user):
        try:
            conf = UserConfig.objects.get(user=user)
            return conf.checked_in
        except UserConfig.DoesNotExist:
            return False



    return user_passes_test(is_checkin, login_url='checkin')
