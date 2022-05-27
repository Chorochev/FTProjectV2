import logging
from typing import Tuple
import psycopg2
import bs_helper as bsh

#log_debud=False
log_debud=True

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
    rows = execute_query("""SELECT a.id, t.type, m.name, w.author, ('<a href=''?article=' || a.id || '''>magazines</a>') as links
                              FROM articles as a INNER JOIN magazines as m ON a.magazines_id = m.id
                                   INNER JOIN article_types as t ON a.article_type_id = t.id
                                   INNER JOIN author as w ON a.author_id = w.id""")    
    return bsh.create_table(rows, ["id","type","name","author", "link"])

def article(id: int):
    if(log_debud): logging.debug("enter 'article()'.")
    rows = execute_query("""SELECT a.id, t.type, m.name, w.author, a.dt, a.headers, a.texts
                              FROM articles as a INNER JOIN magazines as m ON a.magazines_id = m.id
                                   INNER JOIN article_types as t ON a.article_type_id = t.id
                                   INNER JOIN author as w ON a.author_id = w.id
                             WHERE a.id = """ + str(id))    
    if(log_debud): logging.debug("exit 'article()'.")                             
    return rows[0]

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

def create_article(id: int):
    if(log_debud): logging.debug("enter 'create_article()'.")
    row = article(id)    
    str_result = "<div>"        
    str_result += "<h1>" + str(row[5]) + "</h1>"
    str_result += "<div><a href='/'>to the main page</a></div>"  
    str_result += "<tr><td><a href='?articles'>back to articles</a></td></tr>" 
    str_result += "<p>id: " + str(row[0]) + "</p>"
    str_result += "<p>type: " + str(row[1]) + "</p>"
    str_result += "<p>name: " + str(row[2]) + "</p>"
    str_result += "<p>author: " + str(row[3]) + "</p>"
    str_result += "<p>datetime: " + str(row[4]) + "</p>"
    str_result += "<div><textarea rows='15' cols='100' disabled>" + str(row[6]) + "</textarea></div>"
    str_result += "</div>"
    if(log_debud): logging.debug("exit 'create_article()'.")
    return str_result
