import logging

def setup_logger(name, log_file, is_bebug=bool(False)):   
 
    handler = logging.FileHandler(log_file) 
    formatter = logging.Formatter("[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s")       
    handler.setFormatter(formatter)
    
    logger = logging.getLogger(name)
    
    if(is_bebug): logger.setLevel(logging.DEBUG)
    else: logger.setLevel(logging.INFO)

    logger.addHandler(handler)

    return logger