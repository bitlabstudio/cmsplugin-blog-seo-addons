"""Tests for the models of the ``cmsplugin_blog_seo_addons`` app."""
from django.test import TestCase

from .factories import EntrySEOAddonFactory, EntrySEOAddonTranslationFactory


class EntrySEOAddonTestCase(TestCase):
    """Tests for the ``EntrySEOAddon`` model class."""
    longMessage = True

    def test_instantiation(self):
        """Test instantiation of the ``EntrySEOAddon`` model."""
        entryseoaddon = EntrySEOAddonFactory()
        self.assertTrue(entryseoaddon.pk)


class EntrySEOAddonTranslationTestCase(TestCase):
    """Tests for the ``EntrySEOAddonTranslation`` model class."""
    longMessage = True

    def test_instantiation(self):
        """Test instantiation of the ``EntrySEOAddonTranslation`` model."""
        entryseoaddontranslation = EntrySEOAddonTranslationFactory()
        self.assertTrue(entryseoaddontranslation.pk)
