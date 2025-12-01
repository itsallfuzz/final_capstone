from django.apps import AppConfig
from .functions.tweet import Tweet


class News2UConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news2u'

    def ready(self):
        import os
        # Only initialize in main process, not autoreloader
        if os.environ.get('RUN_MAIN') == 'true':
            # Tweet ()
            # Twitter integration is disabled in the Docker file
            # To enable, add you API keys and uncomment Tweet ()
            pass