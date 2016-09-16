#! /usr/bin/env python
import os
import MySQLdb
import re
from datetime import datetime
import time

dic = {
	'Jan': '01',
	'Feb': '02',
	'Mar': '03',
	'Apr': '04',
	'May': '05',
	'Jun': '06',
	'Jul': '07',
	'Oct': '10',
	'Nov': '11',
	'Dec': '12',
	'Aug': '08',
	'Sep': '09',
}

bad_bots  = []
good_bots = []


def preliminary_test():
	"""
	This evaluates whether the request contains a user agent
	or not. 
	"""
	conn = MySQLdb.connect(host = "localhost", user = "root",
                            passwd = "root", db = "botanalyzer")
	cursor = conn.cursor()
	p = "-"
	#import pdb;pdb.set_trace()
	description_bad_ip = 'Empty user agent'
	description_good_ip = 'Ajax requests'
	cursor.execute("SELECT distinct(host), date_time from readlog_logconfig  where user_agents like %s group by host",(p))

	data = cursor.fetchall()
	count = 0
	temp = []
	for row in data:
		ip = data[count]
		temp.append(ip)
		count+=1

	print len(temp)

	for i in range(len(temp)):
		print temp[i][0]
		cursor.execute("SELECT count(*) from readlog_logconfig where host = %s",[temp[i][0]])
		c1 = cursor.fetchall()
		hits = c1[0][0]
		cursor.execute("INSERT INTO readlog_badbotsip (host, Description, date_time, hits) VALUES (%s,%s,%s,%s)",(str(temp[i][0]), description_bad_ip, temp[i][1], hits))

	
	local_host = '127.0.0.1'
	cursor.execute("delete from readlog_badbotsip where host = %s",[local_host])
	conn.commit()
	print "Preliminary test done."


def botAndIp():

	conn = MySQLdb.connect(host = "localhost", user = "root",
							passwd = "root", db = "botanalyzer")

	cursor = conn.cursor()
	a=['%googlebot%', '%Mozilla/xintellibot%','%Twitterbot%', '%bitlybot%', '%bitlybot/2.0%', '%msnbot%','%bing%','%facebookexternalhit%']
	b=['66.249.6|66.249.7|64.68.90|64.233.173.2|216.239.51.9|207.46.13.1|157.55.39|115.249', '194.90.251.114|194.90.251.117|194.90.251.115|194.90.251.113|194.90.251.116' , '149.154.167|199.16.156.124|199.16.156.125|199.16.156.126|199.59.148.209|199.59.148.210|199.59.148.211|199.59.149.21|199.59.149.45', '23.21.3.171|54.237.43.151|50.17.151.94|50.17.69.56|107.20.32.80|54.227.49.251|54.198.188.134|54.224.44.111|54.235.40.139|184.72.158.161','54.147.4.25|50.19.1.73|54.242.155.200|184.72.159.8', '65.55|65.54|131.107|157.55|202.96.51|199.30.17','65.52|65.55|131.253|157.55|157.56|199.30|207.46|74.204|1.39|1.18|117.24|136.18|101.2|72.21|41.2|107.18|14.139','173.252|69.171.2|31.13|66.220']
	length = len(a)
	print len(a)
	print len(b)

	desc=['googlebot','Mozilla/xintellibot','Twitterbot', 'bitlybot', 'bitlybot/2.0','msnbot','bingbot','facebookexternalhit']
	count = 0
	
	for i in range(length):
		temp = []
		hitslist = []
		cursor.execute("select distinct(host), date_time, count(*) from readlog_logconfig where user_agents like %s and host REGEXP %s group by host",(a[i],b[i]))
		data= cursor.fetchall()
		date_list = []
		print a[i]," : ",len(data)
		
		for x  in range(len(data)):
			temp.append(data[x][0])
			date_list.append(data[x][1])
			hitslist.append(data[x][2])
		
		for p in range(len(temp)):

			cursor.execute("INSERT INTO readlog_goodbots (host, Description, date_time, hits) VALUES (%s,%s,%s,%s)",(temp[p], desc[count], date_list[p], hitslist[p]))

		count+=1

	conn.commit()
	print "Good bots done"

def scrappers():

	conn = MySQLdb.connect(host = "localhost", user = "root",
							passwd = "root", db = "botanalyzer")

	cursor = conn.cursor()


	a1='Offline Explorer|SiteSnagger|WebCopier|WebReaper|WebStripper|WebZIP|TeleportPro|Xaldon_WebSpider'
	#a = 'Offline Explorer|qwant|Grapeshot|DotBot|OrangeBot|CrystalSemanticsBot'
	a = ['Offline Explorer','qwant','Grapeshot','DotBot','OrangeBot','CrystalSemanticsBot','rogerbot','GarlikCrawler','MojeekBot']	
	#import pdb;pdb.set_trace()
	for x in range(len(a)):
		cursor.execute("select distinct(host), user_agents, date_time from readlog_logconfig where user_agents REGEXP %s group by host",[a[x]])
		data= cursor.fetchall()
	
		for i in range(len(data)):
			ips = str(data[i][0])
			#scr = str(data[i][1])
			scr = a[x]
			dts = data[i][2]
			des = scr + " Scrapper"


			cursor.execute("SELECT count(*) from readlog_logconfig where host = %s",[ips])
			c1 = cursor.fetchall()
			hits = c1[0][0]

			#cursor.execute("INSERT INTO readlog_badbotsip (host, Description, date_time, hits) VALUES (%s,%s,%s,%s)",(ips,des,dts, hits))
			
			cursor.execute("INSERT INTO readlog_badbotsip_test (host, Description, date_time, hits) VALUES (%s,%s,%s,%s) ON DUPLICATE KEY UPDATE host = %s, Description = %s, date_time = %s, hits = %s",[ips,des,dts, hits,ips,des,dts, hits])

	conn.commit()
	print "Scrappers found"

def badbot_agents():

	conn = MySQLdb.connect(host = "localhost", user = "root",
							passwd = "root", db = "botanalyzer")

	cursor = conn.cursor()

	b = ['MJ12bot','ExaBot','ia_archiver','nutch','AhrefsBot','Python-urllib','oBot','wget','UniversalFeedParser','DigExt','curl','unknown','python-requests','spbot','Java/1.','newrelic']
	gg = set()
	for i in range(len(b)):
		cursor.execute("select distinct(host), date_time from readlog_logconfig where user_agents REGEXP %s group by host",[b[i]])
		data= cursor.fetchall()
		
		print len(data)
		for x in range(len(data)):
			ips = str(data[x][0])
			scr = b[i]
			dts = data[x][1]
			des = str(scr)

			cursor.execute("SELECT count(*) from readlog_logconfig where host = %s",[ips])
			c1 = cursor.fetchall()
			hits = c1[0][0]

			#cursor.execute("INSERT INTO readlog_badbotsip (host, Description, date_time, hits) VALUES (%s,%s,%s,%s)",(ips,des,dts,hits))
			cursor.execute("INSERT INTO readlog_badbotsip (host, Description, date_time, hits) VALUES (%s,%s,%s,%s) ON DUPLICATE KEY UPDATE host = %s, Description = %s, date_time = %s, hits = %s",[ips,des,dts,hits,ips,des,dts,hits])
	conn.commit()

def check():
	start = time.time()
	print start
	preliminary_test()
	botAndIp()
	scrappers()
	badbot_agents()
	end = time.time()
	print end - start

if __name__ == '__main__':
	check()
