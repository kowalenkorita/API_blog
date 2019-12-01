from django.contrib.auth.models import BaseUserManager

__all__ = (
    'UserManager',
)


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra):
        if not username:
            raise ValueError('Username is required')

        if not password:
            raise ValueError('Password is required')

        user = self.model(username=username, **extra)
        user.set_password(password)
        user.save()

        return user

    def create(self, **kwargs):
        return self.create_user(**kwargs)

    def create_user(self, username, password, **extra):
        extra.setdefault('is_staff', False)
        extra.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra)

    def create_superuser(self, username, password, **extra):
        extra.setdefault('is_staff', True)
        extra.setdefault('is_superuser', True)

        if not extra.get('is_staff'):
            raise ValueError('Superuser must have is_staff = True')

        if not extra.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser = True')

        return self._create_user(username, password, **extra)
