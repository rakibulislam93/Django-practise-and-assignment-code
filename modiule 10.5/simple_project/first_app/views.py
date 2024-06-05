from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from datetime import datetime
def home(request):
    # return HttpResponse('This is first_app home page')
    test ={'name':'rakibul','age': 18 , 'date': datetime.now(),'empt':"",
           'student':[{
               'name':'rakib',
               'age': 15
           },
           {
               'name' : 'arif',
               'age' : 20
           },
           {
               'name' : 'nahid',
               'age' : 25
           }],
           'val':['python','is','fun'],
           'numbers':['5','10','15']
           }
    return render(request,'home.html',test)



def about(request):
    # return HttpResponse('This is first_app about page')
    return render(request,'about.html')

def contact(request):
    # return HttpResponse('This is first_app contact page')
    return render(request,'contact.html')

