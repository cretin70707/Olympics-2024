from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, AthletesSerializer, EventsSerializer, MedalsSerializer, SchedulesSerializer, TeamsSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Athletes, Events, Medals, Schedules, Teams
from django_filters.rest_framework import DjangoFilterBackend


      
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

        
class AthletesListView(generics.ListAPIView):
    queryset = Athletes.objects.all()
    serializer_class = AthletesSerializer
    permission_classes = [AllowAny]

class AthleteDetailView(generics.RetrieveAPIView):
    queryset = Athletes.objects.all()
    serializer_class = AthletesSerializer
    lookup_field = 'code'  # Use 'code' as the identifier (replace with your primary key)
    permission_classes = [AllowAny]
    
# List and Detail Views for Events
class EventsListView(generics.ListAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
    permission_classes = [AllowAny]

class EventDetailView(generics.RetrieveAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
    lookup_field = 'event_id'
    permission_classes = [AllowAny]

# List Views for Medallists
class MedalsListView(generics.ListAPIView):
    queryset = Medals.objects.all()
    serializer_class = MedalsSerializer
    permission_classes = [AllowAny]

# List Views for Schedules
class SchedulesListView(generics.ListAPIView):
    queryset = Schedules.objects.all()
    serializer_class = SchedulesSerializer
    permission_classes = [AllowAny]

# List Views for Teams
class TeamsListView(generics.ListAPIView):
    queryset = Teams.objects.all()
    serializer_class = TeamsSerializer 
    permission_classes = [AllowAny] 
      