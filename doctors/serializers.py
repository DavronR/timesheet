from .models import User, Location, HourCode, Activity
from rest_framework import serializers 



class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class HourCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HourCode
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ["id", "username", "email", "first_name", "last_name", "password",]
        extra_kwargs = {"password": {"write_only": True}, "id": {"read_only": True}}



    def create(self, validated_data):
        user = User(email=validated_data["email"],
                    username=validated_data["username"],
                    first_name = validated_data["first_name"], 
                    last_name=validated_data["last_name"],
                    is_doctor=True)
        user.set_password(validated_data["password"])
        user.save() 
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        return instance


class ActivitySerializer(serializers.ModelSerializer):
    is_locked = serializers.SerializerMethodField()
    hours_worked = serializers.SerializerMethodField()
    location_name = serializers.SerializerMethodField(read_only=True)
    doctor_name = serializers.SerializerMethodField(read_only=True)
    hour_code_name = serializers.SerializerMethodField(read_only=True)
    sector = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = "__all__"
        extra_kwargs = {"location": {"write_only": True}, "user": {"write_only": True}, "hour_code": {"write_only": True}}


    def get_is_locked(self, obj):
        return obj.is_locked()
    
    def get_hours_worked(self, obj):
        return obj.hours_worked()
    
    def get_location_name(self, obj):
        loc = Location.objects.get(pk=obj.location.id)
        return loc.name 
    
    def get_sector(self, obj):
        loc = Location.objects.get(pk=obj.location.id)
        return loc.sector 
    
    def get_doctor_name(self, obj):
        doc = User.objects.get(pk=obj.user.id)
        return f"{doc.first_name} {doc.last_name}"
    
    def get_hour_code_name(self, obj):
        h_code = HourCode.objects.get(pk=obj.hour_code.id)
        return h_code.name 










    
    

