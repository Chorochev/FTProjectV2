import bs_loger
from typing import Tuple
import psycopg2
import bs_helper as bsh

controler_log = bs_loger.setup_logger("bs_controller", "/var/local/logs/bookshelf.controler.log", False)

str_connect="dbname='bookshelf' user='postgres' host='DatabaseFT.local' password='postgres'"

#----------- query -----------
def execute_query_insert(query: str):    
    controler_log.debug("enter 'execute_query_insert()'.")
    conn = psycopg2.connect(str_connect)
    cur = conn.cursor()
    cur.execute(query)      
    conn.commit()
    cur.close()
    conn.close()
   
def execute_query(query: str):    
    controler_log.debug("enter 'execute_query()'.")
    conn = psycopg2.connect(str_connect)
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()   
    cur.close() 
    conn.close()
    return rows    

#----------- magazines -----------
def get_magazines(): return execute_query("SELECT m.id, m.name from magazines as m ORDER BY m.id")      

def get_magazines_table(isheader=bool(True)):
    rows = get_magazines()  
    if(isheader): return bsh.create_table_with_header(rows, ["id","name"], "magazines")
    else: return bsh.create_table(rows, ["id","name"])

def insert_magazine(val_name: str):
    controler_log.debug("enter 'insert_magazine()'.")        
    execute_query_insert("INSERT INTO magazines (name) VALUES('" + val_name + "')")  

#----------- article_types -----------
def get_article_types(): return execute_query("SELECT id, type from article_types ORDER BY id")    
  
def get_article_types_table(isheader=bool(True)):
    rows = get_article_types()
    if(isheader): return bsh.create_table_with_header(rows, ["id","type"], "article_types")
    else: return bsh.create_table(rows, ["id","type"])

def insert_article_type(val_type: str):
    controler_log.debug("enter 'insert_article_type()'.")  
    execute_query_insert("INSERT INTO article_types (type) VALUES('" + val_type + "')")       

#----------- authors -----------
def get_authors(): return execute_query("SELECT id, author from author ORDER BY id")    
    
def get_authors_table(isheader=bool(True)):
    rows = get_authors()   
    if(isheader): return bsh.create_table_with_header(rows, ["id","author"], "authors")    
    else: return bsh.create_table(rows, ["id","author"])    

def insert_author(val_author: str):
    controler_log.debug("enter 'insert_author()'.")  
    execute_query_insert("INSERT INTO author (author) VALUES('" + val_author + "')")   

#----------- articles -----------
def get_articles_table(isheader=bool(True)):
    controler_log.debug("enter 'articles()'.")
    sql_query = "SELECT a.id, t.type, m.name, w.author, "
    if(isheader): sql_query += "('<a href=''?article=' || a.id || '''>article</a>') as links"
    else: sql_query += "('<a href=''/static/articles/' || a.id || '/index.html''>article</a>') as links"
    sql_query += """ FROM articles as a INNER JOIN magazines as m ON a.magazines_id = m.id
                                   INNER JOIN article_types as t ON a.article_type_id = t.id
                                   INNER JOIN author as w ON a.author_id = w.id
                             ORDER BY a.dt, a.id"""

    rows = execute_query(sql_query)    
    if(isheader): return bsh.create_table_with_header(rows, ["id","type","name","author", "link"], "articles")
    else: return bsh.create_table(rows, ["id","type","name","author", "link"])

def get_articles(id: int):
    controler_log.debug("enter 'article()'.")
    sql_query = """SELECT a.id, t.type, m.name, w.author, a.dt, a.headers, a.texts
                              FROM articles as a INNER JOIN magazines as m ON a.magazines_id = m.id
                                   INNER JOIN article_types as t ON a.article_type_id = t.id
                                   INNER JOIN author as w ON a.author_id = w.id """
    if(id >= 0): sql_query += " WHERE a.id = """ + str(id) 
    rows = execute_query(sql_query)    
    controler_log.debug("exit 'article()'.")                             
    return rows

def get_article_table(id: int):     
    controler_log.debug("enter 'create_article()'.")
    row = get_articles(id)[0]    
    str_result = "<div>"        
    str_result += "<h1>" + str(row[5]) + "</h1>"
    str_result += "<div><a href='/'>to the main page</a></div>"  
    str_result += "<tr><td><a href='?articles'>back to articles</a></td></tr>" 
    str_result += "<p>id: " + str(row[0]) + "</p>"
    str_result += "<p>type: " + str(row[1]) + "</p>"
    str_result += "<p>name: " + str(row[2]) + "</p>"
    str_result += "<p>author: " + str(row[3]) + "</p>"
    str_result += "<p>date of publication: " + str(row[4]) + "</p>"
    str_result += "<div><textarea rows='15' cols='100' disabled>" + str(row[6]) + "</textarea></div>"
    str_result += "</div>"
    controler_log.debug("exit 'create_article()'.")
    return str_result

def insert_article(magazines_id: int, article_type_id: int, author_id: int, headers: str, texts: str):
    controler_log.debug("enter 'insert_author()'.")  
    execute_query_insert("""INSERT INTO articles 
                            (magazines_id, article_type_id, author_id, headers, texts) 
                            VALUES(""" + str(magazines_id) + """,
                            """ + str(article_type_id) + """,
                            """ + str(author_id) + """,
                            '""" + headers + """',
                            '""" + texts + """')""")       

#----------- all_links -----------
def all_links():
    controler_log.debug("enter 'all_links()'.")
    str_result = "<table>"    
    str_result += "<tr><td><a href='/static/index.html'>static version</a></td></tr>"
    str_result += "<tr><td>&nbsp;</td></tr>"
    str_result += "<tr><td><a href='?magazines'>magazines</a></td></tr>"
    str_result += "<tr><td><a href='?article_types'>article types</a></td></tr>"
    str_result += "<tr><td><a href='?authors'>authors</a></td></tr>"
    str_result += "<tr><td><a href='?articles'>articles</a></td></tr>"
    str_result += "</table>"
    controler_log.debug("exit 'all_links()'.")  
    return str_result
    
    