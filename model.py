#encoding:  utf-8
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence

Base = declarative_base()

# Define data module.

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True)
    name = Column(String)

    def __init__(self,name):
        self.name = name


class GrdJob(Base):
    __tablename__ = 'jobids'
    id = Column(Integer,primary_key=True)
    qname = Column(String)
    hostname = Column(String)
    group = Column(String)
    owner = Column(String)
    jobname = Column(String)
    jobnumber = Column(String)
    account = Column(String)
    priority = Column(String)
    qsub_time = Column(String)
    start_time = Column(String)
    end_time = Column(String)
    ru_utime = Column(String)
    ru_stime = Column(String)
    ru_maxrss = Column(String)
    ru_minflt = Column(String)
    ru_majflt = Column(String)
    ru_nswap = Column(String)
    ru_inblock = Column(String)
    ru_oublock = Column(String)
    ru_msgsnd = Column(String)
    ru_msgrcv = Column(String)
    ru_nsignals = Column(String)
    ru_nvcsw = Column(String)
    ru_nivcsw = Column(String)
    project = Column(String)
    department = Column(String)
    deleted_by = Column(String)
    slots = Column(String)
    failed = Column(String)
    cpu = Column(String)
    mem = Column(String)
    io = Column(String)
    iow = Column(String)
    jc_name = Column(String)
    cwd = Column(String)
    submit_cmd = Column(String)
    ioops = Column(String)

    def __init__(self,qname, hostname, group, owner, jobname, jobnumber, account, priority, qsub_time, start_time, end_time, ru_utime, ru_stime, ru_maxrss, ru_minflt, ru_majflt, ru_nswap, ru_inblock, ru_oublock, ru_msgsnd, ru_msgrcv, ru_nsignals, ru_nvcsw, ru_nivcsw, project, department, deleted_by, slots, failed, cpu, mem, io, iow, jc_name, cwd, submit_cmd, ioops):
        # print jobnumber

        self.qname = qname
        self.hostname = hostname
        self.group = group
        self.owner = owner
        self.jobname = jobname
        self.jobnumber = jobnumber
        self.account = account
        self.priority = priority
        self.qsub_time = qsub_time
        self.start_time = start_time
        self.end_time = end_time
        self.ru_utime = ru_utime
        self.ru_stime = ru_stime
        self.ru_maxrss = ru_maxrss
        self.ru_minflt = ru_minflt
        self.ru_majflt = ru_majflt
        self.ru_nswap = ru_nswap
        self.ru_inblock = ru_inblock
        self.ru_oublock = ru_oublock
        self.ru_msgsnd = ru_msgsnd
        self.ru_msgrcv = ru_msgrcv
        self.ru_nsignals = ru_nsignals
        self.ru_nvcsw = ru_nvcsw
        self.ru_nivcsw = ru_nivcsw
        self.project = project
        self.department = department
        self.deleted_by = deleted_by
        self.slots = slots
        self.failed = failed
        self.cpu = cpu
        self.mem = mem
        self.io = io
        self.iow = iow
        self.jc_name = jc_name
        self.cwd = cwd
        self.submit_cmd = submit_cmd
        self.ioops = ioops


