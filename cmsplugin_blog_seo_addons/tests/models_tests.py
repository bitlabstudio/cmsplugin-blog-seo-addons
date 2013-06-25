"""Tests for the models of the ``cmsplugin_blog_seo_addons`` app."""
from django.test import TestCase

from .factories import SEOAddonFactory, SEOAddonTranslationFactory


class SEOAddonTestCase(TestCase):
    """Tests for the ``SEOAddon`` model class."""
    longMessage = True

    def test_instantiation(self):
        """Test instantiation of the ``SEOAddon`` model."""
        seoaddon = SEOAddonFactory()
        self.assertTrue(seoaddon.pk)


class SEOAddonTranslationTestCase(TestCase):
    """Tests for the ``SEOAddonTranslation`` model class."""
    longMessage = True

    def test_instantiation(self):
        """Test instantiation of the ``SEOAddonTranslation`` model."""
        seoaddontranslation = SEOAddonTranslationFactory()
        self.assertTrue(seoaddontranslation.pk)
