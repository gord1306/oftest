import json, subprocess, sys, os, logging, inspect

#value need change
test_case_name="40.150"
#get datapath switch IP
if len(sys.argv) -1 <=0:
    datapath="tcp:192.168.1.2:6633"
else:
    datapath = "tcp:"+str(sys.argv[1])

log_file_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))+"/log/"+test_case_name+".log"
#remove old log file
if os.path.isfile(log_file_path):
    os.remove(log_file_path)
    
logging.basicConfig(filename=log_file_path, level=logging.INFO)
logger = logging.getLogger(test_case_name)


#try to set config OFPC_FRAG_REASM, to verify has erro return or not
logger.info("dpctl %s set-config flags=0x2"%datapath)
tmp=subprocess.Popen("dpctl %s set-config flags=0x2"%datapath, shell=True, stdout=subprocess.PIPE).stdout.read()
logger.info(tmp)
if len(tmp) !=0:
    d=json.loads(tmp)
    
logger.info("dpctl %s get-config"%datapath)
tmp=subprocess.Popen("dpctl %s get-config"%datapath, shell=True, stdout=subprocess.PIPE).stdout.read()
logger.info(tmp)
if len(tmp) != 0:
    d=json.loads(tmp)
    flags_get_config=int(d["RECEIVED"]["conf"]["flags"], 0)
    if flags_get_config != 0x2:
        logger.info("Get config %d is not the same as set config 0x02"%flags_get_config)
        sys.exit()

logger.info("dpctl %s features"%datapath)
tmp=subprocess.Popen("dpctl %s features"%datapath, shell=True, stdout=subprocess.PIPE).stdout.read()
logger.info(tmp)
if len(tmp) != 0:
    d=json.loads(tmp)
    flags_feature=int(d["RECEIVED"]["caps"], 0)
    if flags_get_config == 0x2:
        if flags_feature&0x20:
            logger.info("PASS")
            print "40.150 -> PASS"
        else:
            logger.info("Fail")
            print "40.150 -> FAIL"    
