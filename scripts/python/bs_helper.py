import bs_loger

update_log = bs_loger.setup_logger("bs_helper", "/var/local/logs/bookshelf.helper.log", False)

def get_params(query_string: str):
    update_log.debug("enter 'get_params()'.") 
    update_log.debug("str='" + query_string + "'") 
    arr_result = []
    if(query_string != ""): 
        for params in query_string.split('&'):
            if(len(params) > 1):
                val = params.split('=')
                if(len(val) > 2):
                    update_log.debug("val[0]='" + val[0] + "'; val[1]='" + val[1] + "'") 
                    arr_result.insert(0, [val[0], val[1]])
    
    update_log.debug("exit 'get_params()'.")     
    return arr_result

def create_table(arr_string: list, headers: list, headerh1: str):
    update_log.debug("enter 'create_table()'.") 
    str_result = "<h3><p style='color:rgb(25,100,25);'>" + headerh1 + " " + str(len(arr_string)) + " items.</p></h3>" 
    str_result += "<div><a href='/'>to the main page</a></div>"
    str_result += "<tr><td><a href='?" + headerh1 + "'>refresh</a></td></tr>"
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
    update_log.debug("exit 'create_table()'.")  
    return str_result
