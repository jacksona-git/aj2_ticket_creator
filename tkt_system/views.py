from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Ticket
from .permissions import IsOwnerOrReadOnly, IsAuthenticated
from .serializers import TicketSerializer
from .pagination import CustomPagination

class get_delete_update_ticket(RetrieveUpdateDestroyAPIView):
    serializer_class = TicketSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)

    #base function to get an object from the model (uses primary key)
    def get_queryset(self, pk):
        try:
            ticket = Ticket.objects.get(pk=pk)
        except Ticket.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return ticket

    # Get a ticket and return serialized data
    def get(self, request, pk):
        ticket = self.get_queryset(pk)
        serializer = TicketSerializer(ticket)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update a ticket
    def put(self, request, pk):
        
        ticket = self.get_queryset(pk)

        if(request.user == ticket.creator): # If creator is who makes request
            serializer = TicketSerializer(ticket, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    # Delete a ticket
    def delete(self, request, pk):

        ticket = self.get_queryset(pk)

        if(request.user == ticket.creator): # If creator is who makes request
            ticket.delete()
            content = {
                'status': 'NO CONTENT'
            }
            return Response(content, status=status.HTTP_204_NO_CONTENT)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)
   

class get_post_tickets(ListCreateAPIView):
    serializer_class = TicketSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination
    
    def get_queryset(self):
       tickets = Ticket.objects.all()
       return tickets

    # Get all tickets
    def get(self, request):
        tickets = self.get_queryset()
        paginate_queryset = self.paginate_queryset(tickets)
        serializer = self.serializer_class(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    # Create a new ticket
    def post(self, request):
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(creator=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

