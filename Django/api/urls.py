from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import Fetch_Device_Info, Fetch_List_of_Locations, Fetch_Location

urlpatterns = {
    path('device_info/', Fetch_Device_Info, name="single_item"),
    path('loc_info/', Fetch_Location, name="Fetch_Location"),
    path('locs_info/', Fetch_List_of_Locations, name="Fetch_Locations")

}
# urlpatterns = format_suffix_patterns(urlpatterns)
