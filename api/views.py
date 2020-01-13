#7
from rest_framework import viewsets, status
from rest_framework.response import Response #8
from rest_framework.decorators import action #8
from django.contrib.auth.models import User #8
from rest_framework.authentication import TokenAuthentication #12
from rest_framework.permissions import IsAuthenticated, AllowAny #19
from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer, UserSerializer #13 userserializer

#13
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )

# Create your views here. 7
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = (TokenAuthentication, ) #12
    permission_classes = (IsAuthenticated, ) #19

    #8
    @action(detail=True, methods=['POST'])
    def rate_movie(self, request, pk=None):
        if 'stars' in request.data:

            movie = Movie.objects.get(id=pk)
            stars = request.data['stars']
            user = request.user #12

            try:
                rating = Rating.objects.get(user=user.id, movie=movie.id)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'rating updated', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
            except:
                rating = Rating.objects.create(user=user, movie=movie, stars=stars)
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'rating created', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)

        else:
            response = {'message': 'you need to provide stars'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = (TokenAuthentication, ) #12
    permission_classes = (IsAuthenticated, ) #19

    #20
    def update(self, request, *args, **kwargs):
        response = {'message': 'you cant update rating like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        response = {'message': 'you cant create rating like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

