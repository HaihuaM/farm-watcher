#!/u/mhaihua/git_workplace/Cache_Grd/ENV/bin/python

import os,re,time,sqlite3,json
from pymongo import MongoClient
# from pymongo import MongoClient

# client = MongoClient('pvdc002', 27017)
# db = client.test_database

# class MongoDB(object):

#     Port = 27017
#     Host = "localhost"

#     def __init__(self, collection):
#         self.collection = collection
#         if self.collection:
#             print "Connecting to mysql..."
#             conn = MongoClient(self.Host, self.Port)
#             # print "Database version: %s" %data
#             db = conn['mydb']
#             my_set = db[self.collection]
#             my_set.insert({"name":"zhangsan","age":18})
#         else:
#             print "PV-INFO: No table specified, exit."
#             sys.exit(0)


# db = MongoDB('testdb_mhaihua')

accf = "accounting"
with open(accf,'rb') as accf_f:
    # contents = accf_f.readlines()
    for lin in accf_f:
        print lin
        # if lin.strip():
        line_splitted = lin.split(':')
        qname = line_splitted[0]
        hostname = line_splitted[1]
        group = line_splitted[2]
        owner = line_splitted[3]
        jobname = line_splitted[4]
        jobnumber = line_splitted[5]
        account = line_splitted[6]
        priority = line_splitted[7]
        qsub_time = line_splitted[8]
        start_time = line_splitted[9]
        end_time = line_splitted[10]
        ru_wallclock = line_splitted[13]
        ru_utime = line_splitted[14]
        ru_stime = line_splitted[15]
        ru_maxrss = line_splitted[16]
        ru_minflt = line_splitted[21]
        ru_majflt = line_splitted[22]
        ru_nswap = line_splitted[23]
        ru_inblock = line_splitted[24]
        ru_oublock = line_splitted[25]
        ru_msgsnd = line_splitted[26]
        ru_msgrcv = line_splitted[27]
        ru_nsignals = line_splitted[28]
        ru_nvcsw = line_splitted[29]
        ru_nivcsw = line_splitted[30]
        project = line_splitted[31]
        department = line_splitted[32]
        deleted_by = line_splitted[33]
        slots = line_splitted[34]
        failed = line_splitted[35]
        cpu = line_splitted[36]
        mem = line_splitted[37]
        io = line_splitted[38]
        iow = line_splitted[40]
        jc_name = line_splitted[41]
        cwd = line_splitted[50]
        submit_cmd = line_splitted[51]
        ru_wallclock = line_splitted[52]
        ioops = line_splitted[53]
        # print hostname,jobname,jobnumber





# class Qacct(object):

#     db = "cacheGrdInfo.db"
#     def __init__(self,grdId,infoLine):
#         self.grdId = grdId
#         self.infoLine = infoLine

#     def _parse_line()



