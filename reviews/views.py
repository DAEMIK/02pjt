from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import ReviewsSerializer
from .models import Reviews


# Create your views here.
@api_view(['GET'])
def review_list(request):
    reviews = Reviews.objects.all()
    serializer = ReviewsSerializer(reviews, many=True)
    return Response(serializer.data)
