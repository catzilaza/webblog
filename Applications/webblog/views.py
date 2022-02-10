from multiprocessing import context
from urllib import response
from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def indexWebblog(request):

    ImageOfHeader = ["webblogPics/scilogo.png", "webblogPics/sciteacher.png"]
    ImagesOfItem  =   [    
                   {'pathPic': "webblogPics/picSeminar1.jpg", 'linkpage': "seminar99708Webblog", 'content' : "สัมมนา 99708"},
                   {'pathPic': "webblogPics/picSeminar2.jpg", 'linkpage': "seminar99709Webblog", 'content' : "สัมมนา 99709"},
                   {'pathPic': "webblogPics/pic3.jpg", 'linkpage': "tourismPhuket", 'content' : "แหล่งท่องเที่ยวจังหวัดภูเก็ต"},
                   {'pathPic': "webblogPics/picSeminar3.jpg", 'linkpage': "researchSources", 'content' : "แหล่งค้นคว้าวิจัย"},
                   {'pathPic': "webblogPics/oldclocktown.png", 'linkpage': "seminar99708Webblog", 'content' : "สัมมนา 99708"},
                   {'pathPic': "webblogPics/pic2.jpg", 'linkpage': "seminar99708Webblog", 'content' : "สัมมนา 99708"},
                   {'pathPic': "webblogPics/pic1.jpg", 'linkpage': "seminar99708Webblog", 'content' : "สัมมนา 99708"},
                   {'pathPic': "webblogPics/pic2.jpg", 'linkpage': "seminar99708Webblog", 'content' : "สัมมนา 99708"},
                   
                ]
    
    
    return render(request, 'indexWebblog.html', 
            {
              'ImageOfHeader0' : ImageOfHeader[0],
              'ImageOfHeader1' : ImageOfHeader[1],
              'Images'  : ImagesOfItem,                               
            }) 

def seminar99708Webblog(request):

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

  return render(request, 'seminar99708Webblog.html',
          {
            'Images'  : ImagesOfItem,
          })
    
def seminar99709Webblog(request):

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

  return render(request, 'seminar99709Webblog.html', 
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

