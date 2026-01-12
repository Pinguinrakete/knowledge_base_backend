from rest_framework import serializers
from knowledge_base.models import Data

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['title', 'text', 'author', 'created_at']
        read_only_fields = ['created_at']
