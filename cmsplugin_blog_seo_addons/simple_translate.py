"""Registering translated models for the ``cmsplugin_blog_seo_addons`` app."""
from simple_translation.translation_pool import translation_pool

from .models import EntrySEOAddon, EntrySEOAddonTranslation


translation_pool.register_translation(EntrySEOAddon, EntrySEOAddonTranslation)
