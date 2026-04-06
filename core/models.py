from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Custom user with optional profile picture and display name.

    Extends Django's AbstractUser so we can attach a profile photo used in the
    portal header dropdown and elsewhere.
    """

    profile_picture = models.ImageField(
        upload_to="profile_pics/",
        blank=True,
        null=True,
        help_text=_("Optional user profile image")
    )
    fee_balance = models.DecimalField(max_digits=9, decimal_places=2, default=0)

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self) -> str:  # pragma: no cover - trivial
        return self.get_full_name() or self.username

# Create your models here.
