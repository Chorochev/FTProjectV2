#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from io import StringIO
import bs_loger
import bs_helper as bsh
import bs_controler as bsc
import datetime

main_log = bs_loger.setup_logger("bookshelf_web", "/var/local/logs/bookshelf.log", False)

def application(environ, start_response):    
    try:    
        main_log.info('Start application. [' + str(environ['REQUEST_METHOD']) + '] ' + str(environ['QUERY_STRING']) + '.')        
        body = "<!DOCTYPE html><html><head><title>Bookshelf</title></head><body>"
        body += "<h1><p style='color:rgb(25,200,25);'>Bookshelf</p></h1>" 
        body += "<h2><p>" + str(datetime.datetime.now()) + "</p></h2>"        
        body += "<div>"     
        
        if(environ['REQUEST_METHOD']) == 'GET':            
            if (environ['QUERY_STRING']) != '':   
                # if(environ['QUERY_STRING'] == 'favicon.ico'):
                #     data = open('/var/www/python_app/favicon.ico', 'rb').read()
                #     start_response('200 OK', [('content-type', 'image/ico'), 
                #                               ('content-length', str(len(data)))])
                #     return [data]
                                    
                # rows = bsh.get_params(environ['QUERY_STRING']) 
                # if(len(rows) > 0): body += bsh.create_table(rows)               

                if(environ['QUERY_STRING'] == 'magazines'): body += bsc.get_magazines_table()
                if(environ['QUERY_STRING'] == 'article_types'): body += bsc.get_article_types_table()
                if(environ['QUERY_STRING'] == 'authors'): body += bsc.get_authors_table()
                if(environ['QUERY_STRING'] == 'articles'): body += bsc.get_articles_table()
                if('article=' in environ['QUERY_STRING']):
                    id = int(str(environ['QUERY_STRING']).split("=")[1])
                    body += bsc.get_article_table(id)

            else:
                body += bsc.all_links()

        body += "</div>"
        body += "</body></html>"
        start_response('200 OK', [('Content-Type','text/html')])
        return body.encode()
    except Exception as e:
        main_log.error(str(e))
        body = "<h1><p style='color:rgb(255,0,0);'>Bookshelf Error</p>" 
        body += str(datetime.datetime.now())
        body += "</h1></br>"
        body += str(e)        
        start_response('200 OK', [('Content-Type','text/html')])
        return body.encode()
