from .models import User, Location, HourCode, Activity
from .serializers import UserSerializer, LocationSerializer, HourCodeSerializer, ActivitySerializer
from rest_framework import viewsets 
from rest_framework import generics
from rest_framework.response import Response



class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all() 
    serializer_class = ActivitySerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_doctor=True)
    serializer_class = UserSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all() 
    serializer_class = LocationSerializer

class HourCodeViewSet(viewsets.ModelViewSet):
    queryset = HourCode.objects.all()
    serializer_class = HourCodeSerializer


   
class ReportView(generics.ListAPIView):
    serializer_class = ActivitySerializer
    
    def get_queryset(self):
        queryset = Activity.objects.all() 
        start = self.request.query_params.get("start", None)
        end = self.request.query_params.get("end", None)
        if start is not None and end is not None:
            queryset = queryset.filter(work_date__range=[start, end])
        return queryset