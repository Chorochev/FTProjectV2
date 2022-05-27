import bs_loger

log_debud=bool(False)
#log_debud=bool(True)

update_log = bs_loger.setup_logger("bs_helper", "/var/local/logs/bookshelf.helper.log")

def get_params(query_string: str):
    if(log_debud): update_log.debug("enter 'get_params()'.") 
    if(log_debud): update_log.debug("str='" + query_string + "'") 
    arr_result = []
    if(query_string != ""): 
        for params in query_string.split('&'):
            if(len(params) > 1):
                val = params.split('=')
                if(len(val) > 2):
                    if(log_debud): update_log.debug("val[0]='" + val[0] + "'") 
                    if(log_debud): update_log.debug("val[1]='" + val[1] + "'") 
                    arr_result.insert(0, [val[0], val[1]])
    
    if(log_debud): update_log.debug("exit 'get_params()'.")     
    return arr_result

def create_table(arr_string: list, headers: list):
    if(log_debud): update_log.debug("enter 'create_table()'.") 
    str_result = "<div><a href='/'>to the main page</a></div>"
    str_result += "<table border='1' bgcolor='#ffcc00'>"   
    str_result += "<tr>"    
    for h in headers:
        str_result += "<th>" + str(h) + "</th>"
    str_result += "</tr>"  
    for row in arr_string:
        str_result += "<tr>"
        for col in row:
                str_result += "<td>"
                str_result += str(col)
                str_result += "</td>"
        str_result += "</tr>"
    
    str_result += "</table>"
    if(log_debud): update_log.debug("exit 'create_table()'.")  
    return str_result
