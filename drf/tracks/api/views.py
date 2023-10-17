# import lib from python

## import from framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import  APIView
from rest_framework.generics import  ListCreateAPIView, RetrieveUpdateDestroyAPIView

# import modules from your app
from tracks.models import Track
from tracks.api.modelserializers import TrackModelSerializer


@api_view(['GET', 'POST'])
def tracks_list(request):
    if request.method == 'GET':
        tracks = Track.get_all_objects()
        serialized_tracks = TrackModelSerializer(tracks, many=True)
        return Response({"data": serialized_tracks.data}, status=status.HTTP_200_OK)


    elif request.method == 'POST':
        serialized_track = TrackModelSerializer(data=request.data)
        if serialized_track.is_valid():
            serialized_track.save()
            return Response({"data": serialized_track.data}, status=status.HTTP_201_CREATED)

        return Response({"errors":serialized_track.errors}, status=status.HTTP_400_BAD_REQUEST)

    else:
        Response({"message": "Request method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)



class TrackAPIView(APIView):

    def get(self, request):

        tracks = Track.get_all_objects()
        serialized_tracks = TrackModelSerializer(tracks, many=True)
        return Response({"data": serialized_tracks.data}, status=status.HTTP_200_OK)

    def post(self,request):
        serialized_track = TrackModelSerializer(data=request.data)
        if serialized_track.is_valid():
            serialized_track.save()
            return Response({"data": serialized_track.data}, status=status.HTTP_201_CREATED)

        return Response({"errors": serialized_track.errors}, status=status.HTTP_400_BAD_REQUEST)



class TrackListCreateAPIView(ListCreateAPIView):
    queryset = Track.get_all_objects()
    serializer_class = TrackModelSerializer


class TrackRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Track.get_all_objects()
    serializer_class = TrackModelSerializer
    lookup_url_kwarg = 'id'