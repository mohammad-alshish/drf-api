from rest_framework import serializers

from .models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        # fields = ['id', 'developer', 'game_name', 'description', 'created_at']
        fields = '__all__'
