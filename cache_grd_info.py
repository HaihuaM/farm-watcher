#!/depot/Python-3.6.2/bin/python 
#encoding:  utf-8

import os,re,time,sqlite3,json,sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import *




# echo flag is a shortcut to setting up SQLAlchemy logging
engine = create_engine('sqlite:///grd.db')
Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)
session = Session()


accf = "accounting.1"

def Accf_Parser(accf):
    with open(accf,'rb') as accf_f:
        for lin in accf_f:
            # print(type(lin))
            line_splitted = lin.split(b':')
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
            cwd = str(line_splitted[50])
            submit_cmd = line_splitted[51]
            ioops = line_splitted[53]

            session.add(GrdJob(qname, hostname, group, owner, jobname, jobnumber, account, priority, qsub_time, start_time, end_time,  ru_utime, ru_stime, ru_maxrss, ru_minflt, ru_majflt, ru_nswap, ru_inblock, ru_oublock, ru_msgsnd, ru_msgrcv, ru_nsignals, ru_nvcsw, ru_nivcsw, project, department, deleted_by, slots, failed, cpu, mem, io, iow, jc_name, cwd, submit_cmd, ioops))
            
            # print qname, hostname, group, owner, jobname, jobnumber, account, priority, qsub_time, start_time, end_time,  ru_utime, ru_stime, ru_maxrss, ru_minflt, ru_majflt, ru_nswap, ru_inblock, ru_oublock, ru_msgsnd, ru_msgrcv, ru_nsignals, ru_nvcsw, ru_nivcsw, project, department, deleted_by, slots, failed, cpu, mem, io, iow, jc_name, cwd, submit_cmd, ioops

            # session.add(tempGrd)
            

    # except:
    #     print "Error: open accouting file failed."
    #     sys.exit(1)


Accf_Parser(accf)
for x in session.query(GrdJob).all():
    print(x.jobnumber)

session.commit()

# class Qacct(object):

#     db = "cacheGrdInfo.db"
#     def __init__(self,grdId,infoLine):
#         self.grdId = grdId
#         self.infoLine = infoLine

#     def _parse_line()



