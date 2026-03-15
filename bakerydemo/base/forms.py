"""
Custom forms for bakerydemo admin interface.

This module provides customizations to Wagtail admin forms,
particularly for handling password reset settings.
"""

from django import forms
from django.conf import settings
from wagtail.users.forms import AuthenticationForm as WagtailAuthenticationForm


class CustomAuthenticationForm(WagtailAuthenticationForm):
    """
    Custom authentication form that respects the WAGTAILUSERS_PASSWORD_RESET_ENABLED setting.
    
    When WAGTAILUSERS_PASSWORD_RESET_ENABLED is False, the password reset link
    will not be shown in the admin login template.
    """
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Store whether password reset is enabled for use in templates
        self.password_reset_enabled = getattr(
            settings, 
            'WAGTAILUSERS_PASSWORD_RESET_ENABLED', 
            True
        )
