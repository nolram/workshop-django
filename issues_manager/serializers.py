from rest_framework import serializers

from .models import Issue


class IssuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['description', 'is_open', 'date_creation', 'date_update', 'user']
        read_only_fields = ['date_creation', 'date_update', 'user']

    def create(self, validated_data):
        validated_data['user'] = self.context.get('request').user
        return super().create(validated_data)