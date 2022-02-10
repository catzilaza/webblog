from django.urls import path
from Applications.webblog.views import indexWebblog, seminarAWebblog, seminarBWebblog, tourismPhuket, researchSources

urlpatterns = [
    path('', indexWebblog, name='indexWebblog'),
    path('seminarAWebblog/', seminarAWebblog, name='seminarAWebblog'),
    path('seminarBWebblog/', seminarBWebblog, name='seminarBWebblog'),
    path('tourismPhuket/', tourismPhuket, name='tourismPhuket'),
    path('researchSources/', researchSources, name='researchSources'),

]