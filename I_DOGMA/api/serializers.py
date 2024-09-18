from rest_framework import serializers

from command.models import Command


class CommandSerializer(serializers.ModelSerializer):
    """Класс-сериализатор для View/Retrieve функций."""

    tags = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        fields = ('id',
                  'author',
                  'name',
                  'syntax',
                  'description',
                  'tags')
        model = Command


class CommandCUDSerializer(serializers.ModelSerializer):
    """Класс-сериализатор для Create/Update/Delete функций."""

    class Meta:
        fields = ('author',
                  'name',
                  'syntax',
                  'description',
                  'tags')
        model = Command
