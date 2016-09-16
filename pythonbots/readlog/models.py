from django.db import models
# from mongoengine import *

# Create your models here.
from django.db import models

# Create your models here.

class LogConfig(models.Model):
	host = models.CharField(max_length=100) #127.0.0.1
	client_id = models.CharField(max_length=100)
	user_id = models.CharField(max_length=100)
	date_time = models.DateTimeField()	          #Datetime
	method = models.CharField(max_length=256) #GET, POST
	endpoint = models.CharField(max_length=256) #admin/login/?next=/admin/
	protocol = models.CharField(max_length=256) #HTTP/1.1
	response_code = models.CharField(max_length=256) #200 status code
	content_size = models.CharField(max_length=256) #1305
	user_agents = models.CharField(max_length=256, default="") #user agent with header
	mobile = models.IntegerField(default=0)
	user_agents_flag = models.IntegerField(default=0)
	section = models.CharField(max_length=256, default="")


class BadBotsIp(models.Model):
	host             = models.CharField(max_length=100) #127.0.0.1
	Description      = models.CharField(max_length=256, default="")
	date_time        = models.DateTimeField(default="1900-01-01 00:00:00")	          #Datetime
	hits             = models.IntegerField(default=0)

class GoodBots(models.Model):
	host             = models.CharField(max_length=100) #127.0.0.1
	Description      = models.CharField(max_length=256,default="")
	date_time        = models.DateTimeField(default="1900-01-01 00:00:00")	          #Datetime
	hits             = models.IntegerField(default=0)

	
# class LogConfig(Document):
# 	host = StringField(max_length=100) #127.0.0.1
# 	client_id = StringField(max_length=100)
# 	user_id = StringField(max_length=100)
# 	date_time = DateTimeField()	          #Datetime
# 	method = StringField(max_length=256) #GET, POST
# 	endpoint = StringField(max_length=256) #admin/login/?next=/admin/
# 	protocol = StringField(max_length=256) #HTTP/1.1
# 	response_code = StringField(max_length=256) #200 status code
# 	content_size = StringField(max_length=256) #1305
# 	user_agents = StringField(max_length=256, default="") #user agent with header
# 	mobile = IntField(default=0)
# 	user_agents_flag = IntField(default=0)
# 	meta = {
# 		'indexes': [{'fields': ['host']}, {'fields': ['user_agents']}]
#     }
# class BadBotsIp(Document):
# 	host = StringField(max_length=100) #127.0.0.1
# 	Description = StringField(max_length=256, default="")
# 	date_time = DateTimeField(default="1900-01-01 00:00:00")	          #Datetime
# 	hits = IntField(default=0)
# 	meta = {
# 		'indexes': [{'fields': ['host']}, {'fields': ['hits']}]
# 	}
# class GoodBots(Document):
# 	host = StringField(max_length=100) #127.0.0.1
# 	Description = StringField(max_length=256,default="")
# 	date_time = DateTimeField(default="1900-01-01 00:00:00")	          #Datetime
# 	hits = IntField(default=0)
# 	meta = {
# 		'indexes': [{'fields': ['host']}, {'fields': ['hits']}]
# 	}
# class training_centroids(Document):
# 	Description = StringField(max_length=256)
# 	centroid1 = FloatField(default=0.0)
# 	centroid2 = FloatField(default=0.0)
# 	centroid3 = FloatField(default=0.0)
# 	count = IntField(default=0)
# 	# deviation = models.FloatField(default=0.0)
# 	# distance = models.FloatField(default=0.0)

# class whois(Document):
# 	host = StringField(max_length=100)
# 	city = StringField(max_length=100)
# 	country = StringField(max_length=100)
# 	isp = StringField(max_length=100)
# 	status = IntField(default=1)
# 	prev_date = DateTimeField()
# 	mod_date = DateTimeField()

# 	meta = {
#         'indexes': [
#             'host'
#         ]
#     }