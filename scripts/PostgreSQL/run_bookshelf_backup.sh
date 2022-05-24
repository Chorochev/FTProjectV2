#!/bin/bash

BACKUP_DIR="/local/files"
ZIP_BACKUP_DIR="/local/backups/bookshelf"
TIMESTAMP=$(date "+%d-%m-%Y_%H-%M-%S")
BACKUP_PATH=$BACKUP_DIR"/"$TIMESTAMP"_backup_bookshelf.sql"
DATABASE_NAME="bookshelf"
LOG="/var/log/postgresql/backup/backup_bookshelf.log"
MAX_COUNT_FILES=3

fun_log()
{
    echo  "["$(date "+%d-%m-%Y %H-%M-%S")"] $1" >> $LOG
}

# backup part
fun_create_bookshelf_backup()
{
    fun_log "Start backup db=bookshelf '"$BACKUP_PATH"'"    
    pg_dump --clean --create --dbname=$DATABASE_NAME > $BACKUP_PATH   
    fun_log "End backup db=bookshelf."
}

# zip part
fun_compress()
{    
    COUNT_FILES=$(find $BACKUP_DIR/*.sql -type f | wc -l)        
    if [[ $COUNT_FILES -gt $MAX_COUNT_FILES ]]
    then
        fun_log "Start compress."
        name_archive=$ZIP_BACKUP_DIR"/"$(date "+%d-%m-%Y_%H-%M-%S")".tar"
        fun_log "Create empty archive '$name_archive'"
        tar -cf $name_archive --files-from /dev/null 
        fun_log "Add files to archive:"
        for item in $(find $BACKUP_DIR/*.sql -type f)
        do
            fun_log "Add to archive: '$item'"
            tar -rf $name_archive --absolute-names $item
            fun_log "Remove: '$item'"
            rm $item
        done
        fun_log "Make zip."
        gzip $name_archive    
        fun_log "End compress."
    fi    
}

# Go
fun_compress
fun_create_bookshelf_backup
