from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from .models import *

from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.db.models import Count
from django.db import connections
from django.db.models import Sum

# Create your views here.
@csrf_exempt
def index(request):

	bad_ips_range = BadBotsIp.objects.count()
	good_ips_range = GoodBots.objects.count()
	hits_in_range = BadBotsIp.objects.values('hits').aggregate(totals = Sum('hits'))['totals']


	bad_hosts = BadBotsIp.objects.all().values('host')
	good_hosts = GoodBots.objects.all().values('host')

	template = loader.get_template('readlog/index.html')
	context = RequestContext(request,{


		'bad_ips_range' : bad_ips_range,
		'good_ips_range' : good_ips_range,
		'hits_in_range' : hits_in_range,
		
		})

	return HttpResponse(template.render(context))






@csrf_exempt
def logins(request):
	template = loader.get_template('readlog/login.html')
	state = "Please log in below..."
	username = password = ''
	if request.POST:
	    username = request.POST.get('username')
	    password = request.POST.get('password')

	    user = authenticate(username=username, password=password)
	    if user is not None:
	        if user.is_active:
	            login(request, user)
	            state = "You're successfully logged in!"
	            return HttpResponseRedirect('/readlog/')
	        else:
	            state = "Your account is not active, please contact the site admin."
	    else:
	        state = "Your username and/or password were incorrect."

	context = RequestContext(request,{
	    	'state':state, 
	    	'username': username,
		})
	return HttpResponse(template.render(context))





@csrf_exempt
def logouts(request):
	auth.logout(request)
	return HttpResponseRedirect('/readlog/login/')



