from django.shortcuts import render

#importing HttpResponse
from django.http import HttpResponse

#create a view (called index)
def index(request):
    # Construct a dictionary to pass to the template engine as its context
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "Cruncy, creamy, cookie, candy, cupcake!"}

    # Return a rendered response to send to client
    # We make use of the shortcut function to make our lives easier
    # Note that the first parameter is the template we wish to use
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
	context_dict = {'boldmessage': "This tutorial has been put together by Ross Johnstone."}
	return render(request, 'rango/about.html', context=context_dict)