import logging

def setup_logger(name, log_file):   
 
    handler = logging.FileHandler(log_file) 
    formatter = logging.Formatter("[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s")       
    handler.setFormatter(formatter)
    
    logger = logging.getLogger(name)
    
    logger.setLevel(logging.DEBUG)

    logger.addHandler(handler)

    return logger