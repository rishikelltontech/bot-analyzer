from django.shortcuts import render
import os
import re
from datetime import datetime
from readlog.models import *
from pymongo import MongoClient

# Create your views here.
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

client = MongoClient('localhost', 27017)
def get_old_access_logs():
	old_log_pattern = '^\[([\w:/]+\s[+\-]\d{4})\] "(\S+) (\S+)\s*(\S*)\s*" (\d{3}) (\S+) (\S+) (\S+) (.*$)'
	date_res = "([^:]+):(\d+:\d+:\d+) ([^\]]+)"
	path = r'access-logs'
	bulk_data = []
	for dir_entry in os.listdir(path):
	    dir_entry_path = os.path.join(path, dir_entry)
	    if os.path.isfile(dir_entry_path):
	        with open(dir_entry_path, 'r') as f:
				count = 0
				text = f.readlines()
				f.close()

				num_lines = sum(1 for line in open(dir_entry_path,'r'))
				print num_lines
				while count < num_lines:
					host_list  = []
					client_id_list = []
					user_id_list = []
					date_time_list = []
					method_list = []
					endpoint_list = []
					protocol_list = []
					response_code_list = []
					content_size_list = []
					user_agents_list = []
					mobile_list = []
					user_agent_flag_list = []
					section_list = []

					req = text[count]
					m = re.findall ( 'httpd: (.*?) -', req)
					p = re.findall('- - (.*$)',req)

					try:
						matchObj = re.match(old_log_pattern,p[0])
					except:
						count+=1
					mobile_string = "Mobile"
					mobile_string_present = 0
					t = "-"
					#print count+1
					if matchObj:
						if len(m)==0:
							pass
						else:
							temp_host = [x.strip() for x in m[0].split(',')]
							if(temp_host[0]=='127.0.0.1' and len( temp_host)>1):
								#host1      = temp_host[1]
								count+=1
								continue
							else:
								host1 = temp_host[0]
							client_id2 = t
							client_id2 = str(client_id2)
							user_id3 = '-'
							date_time4 = matchObj.group(1)
							method5 = matchObj.group(2)
							endpoint6 = matchObj.group(3)
							protocol7 = matchObj.group(4)
							response_code8 = matchObj.group(5)
							content_size9 = matchObj.group(6)
							h = matchObj.group(9)
							m = h.split('"')
							user_agents10  = matchObj.group(8) + " " + m[0]
							if ('"-"' in user_agents10):
								user_agents10 = '-'
								print user_agents10
							user_agent_string = str(user_agents10)

							user_agent_flag = 0
							if(user_agents10):
								user_agent_flag = 1

							if mobile_string in user_agent_string:
								mobile_string_present = 1

							mobile11 = mobile_string_present
							temp_section = endpoint6.split('/')
							if(temp_section[1] == ''):
								section11 = "/" + temp_section[1]
							else:
								section11 = "/" + temp_section[1] + "/"

							temp = re.match(date_res,date_time4, re.M|re.I)
							x1 = temp.group(1)
							x2 = temp.group(2)
							x3 = temp.group(3)
							x4 = x1.split('/')
							x4[1] = dic[x4[1]]

							x5 = x4[1] + " " + x4[0] + " " + x4[2] + " " + x2

							date_time4 = datetime.strptime(x5,'%m %d %Y %H:%M:%S')
							dates = str(date_time4)
							mobiles = str(mobile11)
							flag = str(user_agent_flag)

							line_to_parse = host1 + " " + client_id2 + " " + user_id3 + " " + dates + " " + method5 + " " + endpoint6 + " " + protocol7 + " " + response_code8 + " " + content_size9 + " " + user_agents10 + " " + mobiles + " " + flag
							db.log_config.insert({"host":host})
							# bulk_data.append(LogConfig(host=host1, client_id=client_id2, user_id=user_id3, date_time=date_time4, method=method5,\
							# 		endpoint=endpoint6, protocol=protocol7, response_code=response_code8, content_size=content_size9, user_agents=user_agents10,\
							# 		mobile=mobile11, user_agents_flag=user_agent_flag))
					else:
						continue
					count = count+1
				print "done"
				f.close()
				#import pdb;pdb.set_trace()
				#LogConfig.objects.insert(bulk_data, load_bulk=True)


if __name__ == '__main__':

	get_old_access_logs()
