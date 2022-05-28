from typing import Tuple
import bs_loger
import bs_controler as bsc
import os

html_log = bs_loger.setup_logger("create_static_html", "/var/local/logs/bookshelf.createstatichtml.log", False)

path_base = "/var/www/python_app"
path_template_base = path_base + "/templates"
path_template_dictionary = path_template_base + "/template_dictionary.html"
path_template_article = path_template_base + "/template_article.html"

path_static_base = path_base + "/static"
path_static_article = path_static_base + "/articles"
path_article = path_static_base + "/articles.html"
path_authors = path_static_base + "/authors.html"
path_magazines = path_static_base + "/magazines.html"
path_article_types = path_static_base + "/article_types.html"
path_articles = path_static_base + "/articles.html"

template_name = "__NAME__"
template_header = "__HEADER__"
template_body = "__BODY__"
template_article_id = "__ARTICLEID__"
template_article_type = "__ARTICLETYPE__"
template_magazine_name = "__MAGAZINENAME__"
template_author_name = "__AUTHORNAME__"
template_date_publication = "__DATEPUBLICATION__"


def create_authors_html():
    html_log.debug("enter 'create_authors_html()'.")      
    try:            
        # create html
        body: str    
        with open(path_template_dictionary, 'r') as file: body = file.read()
        body = body.replace(template_name, "Authors")
        body = body.replace(template_header, "Authors")
        body = body.replace(template_body, bsc.get_authors_table(False))
        #save html
        with open(path_authors, 'w') as file: file.write(body)

        html_log.debug("create '" + path_authors + "'.") 
    except Exception as e:
        html_log.error(str(e))

def create_magazines_html():
    html_log.debug("enter 'create_magazines_html()'.")      
    try:            
        # create html
        body: str    
        with open(path_template_dictionary, 'r') as file: body = file.read()
        body = body.replace(template_name, "Magazines")
        body = body.replace(template_header, "Magazines")
        body = body.replace(template_body, bsc.get_magazines_table(False))
        #save html
        with open(path_magazines, 'w') as file: file.write(body)

        html_log.debug("create '" + path_magazines + "'.") 
    except Exception as e:
        html_log.error(str(e))   

def create_article_types_html():
    html_log.debug("enter 'create_article_types_html()'.")      
    try:            
        # create html
        body: str    
        with open(path_template_dictionary, 'r') as file: body = file.read()
        body = body.replace(template_name, "Article types")
        body = body.replace(template_header, "Article types")
        body = body.replace(template_body, bsc.get_article_types_table(False))
        #save html
        with open(path_article_types, 'w') as file: file.write(body)

        html_log.debug("create '" + path_article_types + "'.") 
    except Exception as e:
        html_log.error(str(e))               

def create_articles_html():
    html_log.debug("enter 'create_articles_html()'.")      
    try:            
        # create html
        body: str    
        with open(path_template_dictionary, 'r') as file: body = file.read()
        body = body.replace(template_name, "Articles")
        body = body.replace(template_header, "Articles")
        body = body.replace(template_body, bsc.get_articles_table(False))
        #save html
        with open(path_articles, 'w') as file: file.write(body)

        html_log.debug("create '" + path_articles + "'.") 
    except Exception as e:
        html_log.error(str(e))               

def create_single_article_html(row: Tuple):
    try:
        # create dir
        idpath = path_static_article + "/" + str(row[0])
        if not os.path.exists(idpath): os.makedirs(idpath)
        # create body
        body: str    
        with open(path_template_article, 'r') as file: body = file.read()
        body = body.replace(template_name, "Article")
        body = body.replace(template_header, str(row[5]))
        body = body.replace(template_article_id, str(row[0]))
        body = body.replace(template_article_type, str(row[1]))
        body = body.replace(template_magazine_name, str(row[2]))
        body = body.replace(template_author_name, str(row[3]))
        body = body.replace(template_date_publication, str(row[4]))
        body = body.replace(template_body, str(row[6]))
        # save html
        file_path = idpath + "/index.html"
        with open(file_path, 'w') as file: file.write(body)

        html_log.debug("create '" + file_path + "'.")         
    except Exception as e:
        html_log.error(str(e)) 

def create_all_articles_html():
    html_log.debug("enter 'create_all_articles_html()'.")      
    try:                    
        if not os.path.exists(path_static_article): os.makedirs(path_static_article)        
        rows = bsc.get_articles(-1)
        for row in rows: create_single_article_html(row)
    except Exception as e:
        html_log.error(str(e))   

def main():
    html_log.info("Run update static html.")         
    create_magazines_html()
    create_article_types_html()
    create_authors_html()
    create_articles_html()
    create_all_articles_html()
    html_log.info("Finish update static html.") 

main()            
    
