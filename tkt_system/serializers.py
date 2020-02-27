from rest_framework import serializers
from .models import Ticket
from django.contrib.auth.models import User


class TicketSerializer(serializers.ModelSerializer):  # create class to serializer model
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Ticket
        fields = ('id', 'problem_desc', 'asset_name', 'asset_id', 'creator')


class UserSerializer(serializers.ModelSerializer):  # create class to serializer usermodel
    tickets = serializers.PrimaryKeyRelatedField(many=True, queryset=Ticket.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'tickets')
