from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated

from command.models import Command
from api.serializers import CommandCUDSerializer, CommandSerializer


class CommandAPIMixin:
    """Класс-базовый миксин для API."""

    queryset = Command.optimal.all()
    authentication_classes = (authentication.TokenAuthentication,
                              authentication.SessionAuthentication,
                              )
    permission_classes = (IsAuthenticated, )


class CommandAPIViewMixin:
    """Класс-миксин для View."""

    serializer_class = CommandSerializer


class CommandAPICUDMixin:
    """Класс-миксин для Create, Update, Delete."""

    serializer_class = CommandCUDSerializer
