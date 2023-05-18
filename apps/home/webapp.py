from django.shortcuts import render
from apps.templates import *

def button(request):

    return render(request,'fetchoption.html')

def output(request):
    
    output_data = "Genius Voice eliminates friction. For years people have had to learn to interact with computers, we turn this around. We teach computers how to interact with humans through voice. This creates a seamless experience without losing the human touch."
    website_link = "Visit our website: " + "https://www.geniusvoice.nl/"
    
    # return render(request,"fetchoption.html",{"output_data":output_data, "website_link":website_link})
  
    # return render(request,"fetchoption.html",{"output_data":output_data, "website_link":website_link})
    return "hello"