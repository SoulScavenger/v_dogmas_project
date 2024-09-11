from rest_framework import serializers

from command.models import Command


class CommandSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id',
                  'author',
                  'name',
                  'syntax',
                  'description',
                  'tags')
        model = Command


class CommandCreateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('author',
                  'name',
                  'syntax',
                  'description',
                  'tags')
        model = Command
