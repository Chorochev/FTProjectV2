import logging
import psycopg2
import bs_helper as bsh

log_debud=False
#log_debud=True

logging.basicConfig(filename="/var/local/logs/bookshelf.debug.controler.log", 
                    level=logging.INFO|logging.DEBUG, 
                    format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
                    datefmt="%d/%b/%Y %H:%M:%S")

str_connect="dbname='bookshelf' user='postgres' host='DatabaseFT.local' password='postgres'"

def execute_query(query: str):
    conn = psycopg2.connect(str_connect)
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()    
    conn.close()
    return rows

def magazines():
    rows = execute_query("SELECT id, name from magazines")  
    return bsh.create_table(rows, ["id","name"])

def article_types():
    rows = execute_query("SELECT id, type from article_types")    
    return bsh.create_table(rows, ["id","type"])

def author():
    rows = execute_query("SELECT id, author from author")    
    return bsh.create_table(rows, ["id","author"])

def articles():
    rows = execute_query("""SELECT a.id, t.type, m.name, w.author
                              FROM articles as a INNER JOIN magazines as m ON a.magazines_id = m.id
                                   INNER JOIN article_types as t ON a.article_type_id = t.id
                                   INNER JOIN author as w ON a.author_id = w.id""")    
    return bsh.create_table(rows, ["id","type","name","author"])

def all_links():
    if(log_debud): logging.debug("enter 'all_links()'.")
    str_result = "<table>"    
    str_result += "<tr><td><a href='?magazines'>magazines</a></td></tr>"
    str_result += "<tr><td><a href='?article_types'>article types</a></td></tr>"
    str_result += "<tr><td><a href='?author'>author</a></td></tr>"
    str_result += "<tr><td><a href='?articles'>articles</a></td></tr>"
    str_result += "</table>"
    if(log_debud): logging.debug("exit 'all_links()'.")  
    return str_result
