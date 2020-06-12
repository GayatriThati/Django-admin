from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):
    dest1 = Destination()
    dest1.name = 'Hyderabad'
    dest1.descp = 'A Food Heaven !!'
    dest1.price = 200
    dest1.img = '../static/travelo/images/destination_4.jpg'
    dest1.offer = True
    
    dest2 = Destination()
    dest2.name = 'Bangalore'
    dest2.descp = 'Amazing Weather !!'
    dest2.price = 400
    dest2.img = '../static/travelo/images/news_5.jpg'
    dest2.offer = False
    
    dest3 = Destination()
    dest3.name = 'Mumbai'
    dest3.descp = 'A City That Never Sleeps  !!'
    dest3.price = 700
    dest3.img = '../static/travelo/images/why_3.jpg'
    dest3.offer = True
    
    '''
    context = {'dest1': dest1,
               'dest2': dest2,
               'dest3': dest3}
    '''
    dests = [dest1,dest2,dest3]
    context = {'dests' : dests}
    return render(request,'travelo/index.html',context)