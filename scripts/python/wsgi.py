#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from io import StringIO
import logging
import bs_helper as bsh
import bs_controler as bsc
import datetime

logging.basicConfig(filename="/var/local/logs/bookshelf.log", 
                    level=logging.INFO, 
                    format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
                    datefmt="%d/%b/%Y %H:%M:%S")

def application(environ, start_response):
    try:        
        logging.info('start application.')        
        body = "<h1><p style='color:rgb(25,200,25);'>Bookshelf</p>" 
        body += str(datetime.datetime.now())
        body += "</h1></br>"
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

                if(environ['QUERY_STRING'] == 'magazines'): body += bsc.magazines()
                if(environ['QUERY_STRING'] == 'article_types'): body += bsc.article_types()
                if(environ['QUERY_STRING'] == 'author'): body += bsc.author()
                if(environ['QUERY_STRING'] == 'articles'): body += bsc.articles()
                
            else:
                body += bsc.all_links()

        body += "</div>"
        start_response('200 OK', [('Content-Type','text/html')])
        return body.encode()
    except Exception as e:
        logging.error(str(e))
        body = "<h1><p style='color:rgb(255,0,0);'>Bookshelf Error</p>" 
        body += str(datetime.datetime.now())
        body += "</h1></br>"
        body += str(e)        
        start_response('200 OK', [('Content-Type','text/html')])
        return body.encode()
