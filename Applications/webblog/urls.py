from django.urls import path
from Applications.webblog.views import indexWebblog, seminarAWebblog, seminarBWebblog, tourismPhuket, researchSources, WebblogFormPage, WebblogFormDetailPage, DashBoardPage

urlpatterns = [
    path('', indexWebblog, name='indexWebblog'),
    path('seminarAWebblog/', seminarAWebblog, name='seminarAWebblog'),
    path('seminarBWebblog/', seminarBWebblog, name='seminarBWebblog'),
    path('tourismPhuket/', tourismPhuket, name='tourismPhuket'),
    path('researchSources/', researchSources, name='researchSources'),
    path('WebblogFormPage/', WebblogFormPage, name='WebblogFormPage'),
    path('WebblogFormDetailPage/', WebblogFormDetailPage, name='WebblogFormDetailPage'),
    path('DashBoardPage/', DashBoardPage, name='DashBoardPage')

]