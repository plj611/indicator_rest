from django.urls import path
#from .views import ListCmdView
#from .views import cmd_list, cmd_detail
#from indicator import views
from . import views


urlpatterns = [
#    path('cmd/', ListCmdView.as_view(), name="cmds-all"),
   path('cmd/', views.Cmd_list.as_view()),
   path('cmd/<str:cmd_id>', views.Cmd_detail.as_view()),
]
