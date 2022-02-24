from multiprocessing import context
from pydoc_data.topics import topics
from urllib import response
from django.shortcuts import render
from django.shortcuts import HttpResponse
from Applications.webblog.models import WebblogForm, WebblogFormModel

import requests

# Create your views here.

def indexWebblog(request):

    ImageOfHeader = ["webblogPics/scilogo.png", "webblogPics/sciteacher.png"]
    ImagesOfItem  =   [    
                   {'pathPic': "webblogPics/picSeminar1.jpg", 'linkpage': "seminarAWebblog", 'content' : "สัมมนา 99708"},
                   {'pathPic': "webblogPics/picSeminar2.jpg", 'linkpage': "seminarBWebblog", 'content' : "สัมมนา 99709"},
                   {'pathPic': "webblogPics/pic3.jpg", 'linkpage': "tourismPhuket", 'content' : "แหล่งท่องเที่ยวจังหวัดภูเก็ต"},
                   {'pathPic': "webblogPics/picSeminar3.jpg", 'linkpage': "researchSources", 'content' : "แหล่งค้นคว้าวิจัย"},
                   {'pathPic': "webblogPics/picForm.png", 'linkpage': "WebblogFormPage", 'content' : "แบบฟอร์ม"},
                   {'pathPic': "webblogPics/picTable.png", 'linkpage': "WebblogFormDetailPage", 'content' : "Detail of Table"},
                   {'pathPic': "webblogPics/picDashBoard.png", 'linkpage': "DashBoardPage", 'content' : "DashBoardPage"},
                   {'pathPic': "webblogPics/picCovid.png", 'linkpage': "DashBoardPageCovid", 'content' : "DashBoardPage แสดงผู้ติดเชื้อโควิดวันนี้"},
                   
                ]
    
    
    return render(request, 'indexWebblog.html', 
            {
              'ImageOfHeader0' : ImageOfHeader[0],
              'ImageOfHeader1' : ImageOfHeader[1],
              'Images'  : ImagesOfItem,                               
            }) 

def seminarAWebblog(request):

  ImagesOfItem  =   [    
                   "webblogPics/picSeminar99708Dec11.jpg",
                   "webblogPics/picSeminar99708Dec25.png",
                   "webblogPics/picSeminar99708Jan7.png",
                   "webblogPics/picSeminar99708Jan8.png",
                   "webblogPics/picSeminar99708Jan9_1.png",
                   "webblogPics/picSeminar99708Jan9_2.png",
                   "webblogPics/pic2.jpg",
                   "webblogPics/pic4.jpg",
                   
                ]

  return render(request, 'seminarAWebblog.html',
          {
            'Images'  : ImagesOfItem,
          })
    
def seminarBWebblog(request):

  ImagesOfItem  =   [    
                   "webblogPics/picSeminar99709Dec.jpg",
                   "webblogPics/picSeminar99709Dec1.jpg",
                   "webblogPics/picSeminar99709Dec2.jpg",
                   "webblogPics/picSeminar99709Dec3.jpg",
                   "webblogPics/picSeminar99709Dec4.jpg",
                   "webblogPics/picSeminar99709Dec5.jpg",
                   "webblogPics/oldclocktown.png",
                   "webblogPics/pic3.jpg",
                   
                ]

  return render(request, 'seminarBWebblog.html', 
          {
            'Images'  : ImagesOfItem,
          })

def tourismPhuket(request):

  ImagesOfItem  =   [    
                   "webblogPics/pic1.jpg",
                   "webblogPics/pic2.jpg",
                   "webblogPics/pic3.jpg",
                   "webblogPics/pic4.jpg",
                   "webblogPics/oldclocktown.png",
                   "webblogPics/pic2.jpg",
                   "webblogPics/oldclocktown.png",
                   "webblogPics/pic3.jpg",
                   
                ]

  return render(request, 'tourismPhuket.html',
          {
            'Images'  : ImagesOfItem,
          })

def researchSources(request):

  ImagesOfItem  =   [    
                   "webblogPics/picWebThaiJo.png",
                   "webblogPics/pic2.jpg",
                   "webblogPics/pic3.jpg",
                   "webblogPics/pic4.jpg",
                   "webblogPics/oldclocktown.png",
                   "webblogPics/pic2.jpg",
                   "webblogPics/oldclocktown.png",
                   "webblogPics/pic3.jpg",
                   
                ]
  return render(request, 'researchSources.html', {
            'Images'  : ImagesOfItem,
  })

def WebblogFormPage(request):

  context = {}
  if request.method == "POST":
        #print('request.POST', request.POST)
        form = WebblogForm(request.POST)
        if form.is_valid():
            form.save()
            print('Save successfully')
        else:
            print('Error')
  form = WebblogForm()
  context['form'] = form
  return render(request, 'WebblogFormPage.html', context)

def WebblogFormDetailPage(request):
  
  contexts = list(WebblogFormModel.objects.values())  
  print(contexts)
  
  return render(request, 'WebblogFormDetailPage.html', {'contexts' : contexts})

def DashBoardPage(request):
  return render(request, 'DashBoardPage.html')

def DashBoardPageCovid(request):

  responseData = requests.get("https://covid19.ddc.moph.go.th/api/Cases/today-cases-all")
  #print(responseData.json())
  data = responseData.json()
  #print("ผู้ติดเชื้อรายใหม่",data[0]['new_case'])

  return render(request, 'DashBoardPageCovid.html', {
        'txn_date' : data[0]['txn_date'],
        'new_case' : data[0]['new_case'],
        'total_case' : data[0]['total_case'],
        'new_case_excludeabroad' : data[0]['new_case_excludeabroad'],
        'total_case_excludeabroad' : data[0]['total_case_excludeabroad'],
        'new_death' : data[0]['new_death'],
        'total_death' : data[0]['total_death'],
        'new_recovered' : data[0]['new_recovered'],
        'total_recovered' : data[0]['total_recovered'],
        'update_date' : data[0]['update_date'],
    })
 