from django.apps import AppConfig


class HomeAppConfig(AppConfig):
    name = 'home_app'

    def ready(self):
        import home_app.signals
