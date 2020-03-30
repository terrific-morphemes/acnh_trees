from django.urls import path
from .views import TreeCreate, TreeUpdate, RegionCreate, RegionUpdate
from .views import TreeList, RegionList
from .views import report_wasp, report_harvest

urlpatterns = [
    path('tree/add/', TreeCreate.as_view(), name='tree-add'),
    path('tree/<int:pk>/', TreeUpdate.as_view(), name='tree-update'),
    path('region/add/', RegionCreate.as_view(), name='region-add'),
    path('region/<int:pk>/', RegionUpdate.as_view(), name='region-update'),
    path('tree/<int:pk>/harvest/', report_harvest, name='report-harvest'),
    path('tree/<int:pk>/wasp/', report_harvest, name='report-wasp'),
    path('tree/', TreeList.as_view(), name='tree-view'),
    path('region/', RegionList.as_view(), name='region-view'),
    path('', TreeList.as_view(), name='tree-view')
]
