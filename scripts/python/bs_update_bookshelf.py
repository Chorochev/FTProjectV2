import bs_loger
import bs_controler as bsc
import random

update_log = bs_loger.setup_logger("bookshelf_update", "/var/local/logs/bookshelf.update.log")

log_debug=bool(True)
#log_debug=bool(False)

path_words="/usr/share/dict/words"
count_words=sum(1 for line in open(path_words))

def get_random_word():
    word=""
    try: 
        if(log_debug): update_log.debug("enter 'get_random_word()'.") 
        random.seed()
        number_line=random.randint(0, count_words)   
        current_line=0
        
        with open(path_words) as f:
            for line in f:
                current_line +=1
                if(current_line >= number_line):
                    word=line
                    break

    except Exception as e:        
        update_log.error("get_random_word => " + str(e))

    return word.replace("\n","")

def get_random_string(length_str: int):
    result_string=get_random_word()   
    while ((len(result_string)) < length_str):
        w = get_random_word()
        result_string += " " + w
       
    return result_string[:length_str]


def add_author():
    if(log_debug): update_log.debug("enter 'add_author()'.") 


def main():
    try:        
        update_log.info('Starting update the bookshelf.')
        for n in range(5):
            word=get_random_word()
            print(word)
        
        for n in range(5):
            word=get_random_string(75)
            print(word)

        update_log.info('The end of updating the bookshelf.')        
    except Exception as e:
        print(str(e))
        update_log.error(str(e))


# run
main()    
