from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Athletes, Events, Medals, Schedules, Teams
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # Add custom claims
        data['username'] = self.user.username
        data['email'] = self.user.email
        return data




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {"password": {"write_only": True}, "email": {"write_only": True}}
    
    #Create a new user
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
 

            
class AthletesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Athletes  
        fields = '__all__'  
              
class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events  
        fields = '__all__'

class MedalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medals  
        fields = '__all__'                      
        
class SchedulesSerializer(serializers.ModelSerializer):
    formatted_start_time = serializers.SerializerMethodField()  # Add custom field
    formatted_end_time = serializers.SerializerMethodField()  # Add custom field
    class Meta:
        model = Schedules  
        fields = '__all__'
    
    def get_formatted_start_time(self, obj):
        if obj.start_date:
            return obj.start_date.strftime('%I:%M %p')  
        return None
    
    def get_formatted_end_time(self, obj):
        if obj.end_date:
            return obj.end_date.strftime('%I:%M %p') 
        return None 
        
class TeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams  
        fields = '__all__'        