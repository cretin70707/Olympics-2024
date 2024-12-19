from django.contrib import admin
from django.urls import path, include
from api.views import (
    CustomTokenObtainPairView,
    CreateUserView, 
    AthleteDetailView,
    EventsListView,
    EventDetailView, 
    SchedulesListView, 
    TeamsListView, 
    MedalsListView, 
    AthletesListView
    )
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/user/register/", CreateUserView.as_view(), name="register"),
    path("api/token/", CustomTokenObtainPairView.as_view(), name="get_token"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh_token"),
    path("api-auth/", include("rest_framework.urls")),
    path('api/athletes/', AthletesListView.as_view(), name='athletes-list'),
    path('api/athletes/<int:code>/', AthleteDetailView.as_view(), name='athletes-list'),
    path('api/events/', EventsListView.as_view(), name='events-list'),
    path('api/medals/', MedalsListView.as_view(), name='medals-list'),
    path('api/schedules/', SchedulesListView.as_view(), name='schedules-list'),
    path('api/teams/', TeamsListView.as_view(), name='teams-list'),
]
