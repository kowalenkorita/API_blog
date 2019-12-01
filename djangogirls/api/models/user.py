from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from api.managers import UserManager

__all__ = (
    'User',
)


class User(AbstractUser):
    objects = UserManager()

    class Meta:
        verbose_name = _('Аккаунт пользователя')
        verbose_name_plural = _('Аккаунты пользователей')

    def __str__(self):
        return self.username
