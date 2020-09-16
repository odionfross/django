from django.shortcuts import render, HttpResponse
from datetime import date, datetime
# from time import gmtime, strftime

# Create your views here.
def index(request):
	context = {
		"time": datetime.now() # "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
	}
	return render(request, "index.html", context) 