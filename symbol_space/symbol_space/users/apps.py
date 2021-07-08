from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "symbol_space.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import symbol_space.users.signals  # noqa F401
        except ImportError:
            pass
