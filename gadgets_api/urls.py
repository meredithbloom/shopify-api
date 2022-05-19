from django.urls import path 
from . import views 


urlpatterns = [
    path('api/gadgets', views.GadgetList.as_view(), name='gadgets_list'),
    path('api/gadgets/<int:pk>', views.GadgetDetail.as_view(), name='gadgets_detail'),
    
    path('api/locations', views.LocationList.as_view(), name='location_list'),
    path('api/locations/<int:pk>', views.LocationDetail.as_view(), name='location_detail'),
]
