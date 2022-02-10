from django.urls import path
from Applications.webblog.views import indexWebblog, seminarAWebblog, seminar99709Webblog, tourismPhuket, researchSources

urlpatterns = [
    path('', indexWebblog, name='indexWebblog'),
    path('seminarAWebblog/', seminarAWebblog, name='seminarAWebblog'),
    path('seminar99709Webblog/', seminar99709Webblog, name='seminar99709Webblog'),
    path('tourismPhuket/', tourismPhuket, name='tourismPhuket'),
    path('researchSources/', researchSources, name='researchSources'),

]