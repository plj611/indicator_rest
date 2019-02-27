from django.urls import path
#from .views import ListCmdView
from .views import cmd_list, cmd_detail
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
#    path('cmd/', ListCmdView.as_view(), name="cmds-all"),
   path('cmd/', cmd_list),
   path('cmd/<str:cmd_id>', cmd_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
