from django.urls import path
from Applications.webblog.views import indexWebblog, seminar99708Webblog, seminar99709Webblog, tourismPhuket, researchSources

urlpatterns = [
    path('', indexWebblog, name='indexWebblog'),
    path('seminar99708Webblog/', seminar99708Webblog, name='seminar99708Webblog'),
    path('seminar99709Webblog/', seminar99709Webblog, name='seminar99709Webblog'),
    path('tourismPhuket/', tourismPhuket, name='tourismPhuket'),
    path('researchSources/', researchSources, name='researchSources'),

]