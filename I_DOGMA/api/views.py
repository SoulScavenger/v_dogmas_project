from rest_framework import generics


from api.mixins import CommandAPIMixin, CommandAPICUDMixin, CommandAPIViewMixin


class CommandAPIView(
        CommandAPIMixin, CommandAPIViewMixin, generics.ListAPIView):
    """Класс-View получение всех объектов сущности Command."""


class CommandAPIRetrieve(
        CommandAPIMixin, CommandAPIViewMixin, generics.RetrieveAPIView):
    """Класс-View получение объекта сущности Command."""


class CommandAPICreate(
        CommandAPIMixin, CommandAPICUDMixin, generics.ListCreateAPIView):
    """Класс-Create создания объекта сущности Command."""


class CommandAPIUpdate(
        CommandAPIMixin, CommandAPICUDMixin, generics.RetrieveUpdateAPIView):
    """Класс-Update обновления объекта сущности Command."""


class CommandAPIDestroy(
        CommandAPIMixin, CommandAPICUDMixin, generics.RetrieveDestroyAPIView):
    """Класс-Destroy удаления объекта сущности Command."""
