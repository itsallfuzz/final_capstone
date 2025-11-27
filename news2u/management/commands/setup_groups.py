from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from news2u.models import Article, Newsletter


class Command(BaseCommand):
    help = 'Set up user groups with appropriate permissions'

    def handle(self, *args, **kwargs):
        article_ct = ContentType.objects.get_for_model(Article)
        newsletter_ct = ContentType.objects.get_for_model(Newsletter)

        # JOURNALIST
        journalist_group, created = Group.objects.get_or_create(
            name='Journalist')
        j_perms = Permission.objects.filter(
            content_type__in=[article_ct, newsletter_ct],
            codename__in=[
                'add_article',
                'change_article',
                'view_article',
                'delete_article',
                'add_newsletter',
                'change_newsletter',
                'view_newsletter',
                'delete_newsletter'
                ]
        )
        journalist_group.permissions.set(j_perms)

        # EDITOR
        editor_group, created = Group.objects.get_or_create(
            name='Editor')
        e_perms = Permission.objects.filter(
            content_type__in=[article_ct, newsletter_ct],
            codename__in=['change_article', 'view_article',
                          'change_newsletter', 'view_newsletter']
        )
        editor_group.permissions.set(e_perms)

        # PUBLISHER
        publisher_group, created = Group.objects.get_or_create(
            name='Publisher')
        p_perms = Permission.objects.filter(
            content_type__in=[article_ct, newsletter_ct],
            codename__in=['view_article', 'change_article',
                          'view_newsletter', 'change_newsletter']
        )
        publisher_group.permissions.set(p_perms)

        # READER
        reader_group, created = Group.objects.get_or_create(
            name='Reader')
        r_perms = Permission.objects.filter(
            content_type__in=[article_ct, newsletter_ct],
            codename__in=['view_article', 'view_newsletter']
        )
        reader_group.permissions.set(r_perms)

        self.stdout.write(self.style.SUCCESS(
            'All groups and permissions set up!'))