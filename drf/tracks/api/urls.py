
from django.urls import  path
from tracks.api.views import (tracks_list, TrackAPIView,
                              TrackListCreateAPIView, TrackRetrieveUpdateDestroyAPIView)
urlpatterns = [

    # path('', tracks_list, name='api.tracks.list')
    # path('', TrackAPIView.as_view())
    path('', TrackListCreateAPIView.as_view()),
    path('<int:id>',TrackRetrieveUpdateDestroyAPIView.as_view() )
]