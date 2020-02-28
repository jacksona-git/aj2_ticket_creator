from django.urls import include, path, re_path
from . import views

#map the url endpoint to the correct view
urlpatterns = [
    re_path(r'^api/v1/tickets/(?P<pk>[0-9]+)$', # Url to get update or delete a ticket
        views.get_delete_update_ticket.as_view(),
        name='get_delete_update_ticket'
    ),
    path('api/v1/tickets/', # urls list all and create new one
        views.get_post_tickets.as_view(),
        name='get_post_tickets'
    )
]
