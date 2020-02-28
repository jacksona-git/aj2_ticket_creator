from rest_framework import serializers
from .models import Ticket
from django.contrib.auth.models import User

#Class to convert ticket model to JSON via serialization
#The model serializer is a special serializer that handle models directly

class TicketSerializer(serializers.ModelSerializer):  # create class to serializer model
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Ticket
        fields = ('id', 'problem_desc', 'asset_name', 'asset_id', 'creator')

#class to serialize user model
class UserSerializer(serializers.ModelSerializer):  
    tickets = serializers.PrimaryKeyRelatedField(many=True, queryset=Ticket.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'tickets')
