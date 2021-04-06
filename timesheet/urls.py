from django.urls import path, include
from django.contrib import admin
from doctors import views 
from rest_framework.routers import DefaultRouter 

router = DefaultRouter()
router.register("doctors", views.DoctorViewSet)
router.register("locations", views.LocationViewSet)
router.register("hourcodes", views.HourCodeViewSet)
router.register("activities", views.ActivityViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/report/", views.ReportView.as_view(), name="report"),
    path("api/", include(router.urls)),

]