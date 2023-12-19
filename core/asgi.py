import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.base')

application = get_asgi_application()

# import os
# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
# from apps.user.routing import websocket_urlpatterns as user_websocket_urlpatterns
# from .routing import websocket_urlpatterns as core_websocket_urlpatterns
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
# django_asgi_app = get_asgi_application()
#
# application = ProtocolTypeRouter({
#     'http': django_asgi_app,
#     'websocket': AuthMiddlewareStack(
#         URLRouter(
#             core_websocket_urlpatterns + user_websocket_urlpatterns
#         )
#     ),
# })