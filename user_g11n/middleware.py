import django
from django.utils import timezone, translation
from django.conf import settings
import pytz


class UserLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_language = settings.LANGUAGE_CODE
        if request.user.is_authenticated:
            user_language = getattr(request.user, 'language', user_language)
            if getattr(settings, "USER_G11N_ATTR_NAME", None):
                user_profile = getattr(
                    request.user,
                    settings.USER_G11N_ATTR_NAME, None)
                if user_profile:
                    user_language = getattr(user_profile, "language", user_language)

        translation.activate(user_language)

        if django.VERSION[0] <= 2:
            request.session[translation.LANGUAGE_SESSION_KEY] = user_language

        response = self.get_response(request)

        if django.VERSION[0] >= 3:
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)

        return response


class UserTimeZoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_anonymous:
            timezone.deactivate()
        user_timezone = getattr(settings,'TIME_ZONE',None)
        if request.user.is_authenticated:
            user_timezone = getattr(request.user, 'timezone', user_timezone)
            if getattr(settings, "USER_G11N_ATTR_NAME", None):
                user_profile = getattr(
                    request.user,
                    settings.USER_G11N_ATTR_NAME, None)
                if user_profile:
                    user_timezone = getattr(user_profile, "timezone", user_timezone)
        if user_timezone:
            timezone.activate(pytz.timezone(user_timezone))

        return self.get_response(request)
