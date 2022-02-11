from multiprocessing import context
from urllib import response
from django.shortcuts import render
from django.shortcuts import HttpResponse
from Applications.webblog.models import WebblogForm, WebblogFormModel

# Create your views here.

def indexWebblog(request):

    ImageOfHeader = ["webblogPics/scilogo.png", "webblogPics/sciteacher.png"]
    ImagesOfItem  =   [    
                   {'pathPic': "webblogPics/picSeminar1.jpg", 'linkpage': "seminarAWebblog", 'content' : "สัมมนา 99708"},
                   {'pathPic': "webblogPics/picSeminar2.jpg", 'linkpage': "seminarBWebblog", 'content' : "สัมมนา 99709"},
                   {'pathPic': "webblogPics/pic3.jpg", 'linkpage': "tourismPhuket", 'content' : "แหล่งท่องเที่ยวจังหวัดภูเก็ต"},
                   {'pathPic': "webblogPics/picSeminar3.jpg", 'linkpage': "researchSources", 'content' : "แหล่งค้นคว้าวิจัย"},
                   {'pathPic': "webblogPics/picForm.png", 'linkpage': "WebblogFormPage", 'content' : "แบบฟอร์ม"},
                   {'pathPic': "webblogPics/oldclocktown.png", 'linkpage': "WebblogFormDetailPage", 'content' : "Detail for Form"},
                   {'pathPic': "webblogPics/pic1.jpg", 'linkpage': "seminarAWebblog", 'content' : "สัมมนา 99708"},
                   {'pathPic': "webblogPics/pic2.jpg", 'linkpage': "seminarAWebblog", 'content' : "สัมมนา 99708"},
                   
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
        #print(request.POST)
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
  #contexts = {}
  #contexts['datas'] = WebblogFormModel.objects.all()  
  #return render(request, 'WebblogFormDetailPage.html', contexts)
  return render(request, 'WebblogFormDetailPage.html')