"""Factories for the ``cmsplugin_blog_seo_addons`` app."""
import factory
from cmsplugin_blog.models import Entry
from django_libs.tests.factories import SimpleTranslationMixin

from ..models import EntrySEOAddon, EntrySEOAddonTranslation


class EntryFactory(factory.Factory):
    """Factory for the ``Entry`` model."""
    FACTORY_FOR = Entry


class BaseEntrySEOAddonFactory(factory.Factory):
    """Factory for the ``EntrySEOAddon`` model."""
    FACTORY_FOR = EntrySEOAddon

    entry = factory.SubFactory(EntryFactory)


class EntrySEOAddonFactory(SimpleTranslationMixin, BaseEntrySEOAddonFactory):
    FACTORY_FOR = EntrySEOAddon

    @staticmethod
    def _get_translation_factory_and_field():
        return (EntrySEOAddonTranslationFactory, 'entryseoaddon')


class EntrySEOAddonTranslationFactory(factory.Factory):
    """Factory for the ``EntrySEOAddonTranslation`` model."""
    FACTORY_FOR = EntrySEOAddonTranslation

    meta_description = factory.Sequence(
        lambda n: 'Meta description {}'.format(n))
    entryseoaddon = factory.SubFactory(BaseEntrySEOAddonFactory)
