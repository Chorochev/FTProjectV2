import bs_loger
import bs_controler as bsc
import random

update_log = bs_loger.setup_logger("bookshelf_update", "/var/local/logs/bookshelf.update.log", False)

path_words="/usr/share/dict/words"
count_words=sum(1 for line in open(path_words))

# ----------------- random -----------------
def get_random_num(max: int):
    random.seed()
    return random.randint(0, max)  

def get_random_word():
    word=""
    try: 
        update_log.debug("enter 'get_random_word()'.")
        number_line=get_random_num(count_words) 
        current_line=0
        
        with open(path_words) as f:
            for line in f:
                current_line +=1
                if(current_line >= number_line):
                    word=line
                    break

    except Exception as e:        
        update_log.error("get_random_word => " + str(e))
    
    return word.replace("\n","").replace("'"," ")

def get_random_string(length_str: int):
    result_string=get_random_word()   
    while ((len(result_string)) < length_str):
        w = get_random_word()
        result_string += " " + w
       
    return result_string[:length_str]

def get_random_author(index: int):
    rows=bsc.get_authors()
    num=get_random_num(len(rows) - 1)
    return rows[num][index]

def get_random_article_type(index: int):
    rows=bsc.get_article_types()
    num=get_random_num(len(rows) - 1)
    return rows[num][index]

def get_random_magazine(index: int):
    rows=bsc.get_magazines()
    num=get_random_num(len(rows) - 1)
    return rows[num][index]    

# ----------------- add -----------------
def add_author():
    update_log.debug("enter 'add_author()'.") 
    val_author=get_random_word()
    bsc.insert_author(val_author)
    update_log.info()("adds a author: '" + val_author + "'.") 

def add_article_type():
    update_log.debug("enter 'add_article_types()'.") 
    val_article_type=get_random_word()
    bsc.insert_article_type(val_article_type)
    update_log.info()("adds a article type: '" + val_article_type + "'.") 
        
def add_magazine():
    update_log.debug("enter 'add_magazine()'.") 
    val_magazine=get_random_word()
    bsc.insert_magazine(val_magazine)  
    update_log.info()("adds a magazine: '" + val_magazine + "'.")    

def add_article():
    update_log.debug("enter 'add_article()'.") 
    magazines_id=get_random_magazine(0)
    article_type_id=get_random_article_type(0)
    author_id=get_random_author(0)
    headers=get_random_string(49)
    texts=get_random_string(499)
    bsc.insert_article(magazines_id, article_type_id, author_id, headers, texts)      

# ----------------- main -----------------
def main():
    try:        
        update_log.info('Starting update the bookshelf.')
       
        if(get_random_num(5) == 3): add_author()
        if(get_random_num(10) == 5): add_article_type()
        if(get_random_num(10) == 7): add_magazine()
        add_article()
        
        update_log.info('Ending of updating the bookshelf.')        
    except Exception as e:
        print(str(e))
        update_log.error(str(e))

# ----------------- run -----------------
main()    
