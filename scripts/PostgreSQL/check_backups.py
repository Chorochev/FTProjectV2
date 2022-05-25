import os
import logging

# Import smtplib for the actual sending function
import smtplib
# Here are the email package modules we'll need
from email.mime.multipart import MIMEMultipart
from xmlrpc.client import boolean

logging.basicConfig(filename="/var/log/postgresql/backup/backup.log", 
                    level=logging.INFO, 
                    format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
                    datefmt="%d/%b/%Y %H:%M:%S")

cwd = os.getcwd()
backup_dir="/local/backups/bookshelf"
#config_path=cwd + "/backups.conf"
config_path="/local/scripts/backups.conf"
# Settings of config
max_count_files=50
max_count_bytes=102400
is_send_mail=True


# create config
def fun_create_config(is_send: boolean):
    try:
        logging.info("Create " + config_path)
        with open(config_path, "w") as file:
            file.write("max_count_files=50" + os.linesep)
            file.write("max_count_bytes=102400" + os.linesep)
            file.write("is_send_mail=" + str(is_send) + os.linesep)
    except Exception as e:
        logging.error("fun_create_config: " + str(e))

# load config
def fun_load_config():
    try:
        #print("fun_load_config")
        with open(config_path) as file:
            for line in file:                
                val=line.rstrip().split("=")
                #print("line=" + line + "; " + "val[0]=" + val[0] + "; val[1]=" + val[1])
                if(val[0] == "max_count_files"): 
                    global max_count_files
                    max_count_files = int(val[1])
                if(val[0] == "max_count_bytes"): 
                    global max_count_bytes
                    max_count_bytes = int(val[1])
                if(val[0] == "is_send_mail"): 
                    global is_send_mail
                    if(val[1] == "True"): is_send_mail=True
                    else: is_send_mail=False
    except Exception as e:
        logging.error("fun_load_config:" + str(e))

# replace config
def fun_replace_config(is_send: boolean):
    try:
        os.remove(config_path)
        fun_create_config(is_send)
    except Exception as e:
        logging.error("fun_replace_config: " + str(e))

# config
def fun_config():
    try:        
        if(os.path.isfile(config_path)): fun_load_config()            
        else: fun_create_config(True)
        logging.info("Run check backups. is_send_mail=" + str(is_send_mail) + ".")
    except Exception as e:
        logging.error("fun_config: " + str(e))

# print values
def fun_print_values():
    try:
        print("cwd=" + cwd)
        print("backup_dir=" + backup_dir)
        print("config_path=" + config_path)
        print("max_count_files=" + str(max_count_files))
        print("max_count_bytes=" + str(max_count_bytes))
        print("is_send_mail=" + str(is_send_mail))
    except Exception as e:
        logging.error("fun_print_values: " + str(e))

def fun_send_email(header: str, body: str):
    try:
        msg = MIMEMultipart()
        msg['Subject'] = header
        # me == the sender's email address
        # family = the list of all recipients' email addresses
        msg['From'] = 'root@DatabaseFT'
        msg['To'] = 'root@DatabaseFT'
        msg.preamble = body
        # Send the email via our own SMTP server.
        s = smtplib.SMTP('localhost')
        s.sendmail('root@DatabaseFT', 'root@DatabaseFT', msg.as_string())
        s.quit()
    except Exception as e:
        logging.error("fun_send_email: " + str(e))

def fun_check_count_files():
    try:
        current_count_files = 0
        for line in os.listdir(backup_dir):
            if(os.path.isfile(os.path.join(backup_dir, line))): current_count_files += 1
        if(current_count_files > max_count_files):            
            if(is_send_mail):
                logging.info("Send mail. current_count_files=" + str(current_count_files))
                header="The count of files from backup"
                body=str(current_count_files) + " files in '" + backup_dir + "'"
                fun_send_email(header, body)
                fun_replace_config(False)
        #print("current_count_files="+ str(current_count_files))
    except Exception as e:
        logging.error("fun_check_count_files: " + str(e))

def fun_check_count_bytes():
    try:
        current_count_bytes = 0
        for line in os.listdir(backup_dir):
            current_count_bytes += os.path.getsize(os.path.join(backup_dir, line))

        if(current_count_bytes > max_count_bytes):            
            if(is_send_mail):
                logging.info("Send mail. current_count_bytes=" + str(current_count_bytes))
                header="The count of files from backup"
                body=str(current_count_bytes) + " bytes in '" + backup_dir + "'"
                fun_send_email(header, body)
                fun_replace_config(False)
        print("current_count_bytes="+ str(current_count_bytes))
    except Exception as e:
        logging.error("fun_check_count_files: " + str(e))        

# Run
fun_config()
#fun_print_values()
fun_check_count_files()
#fun_print_values()
fun_check_count_bytes()
