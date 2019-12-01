from rest_framework.authentication import SessionAuthentication

__all__ = (
    'NoCSRFSessionAuthentication',
)


class NoCSRFSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return
