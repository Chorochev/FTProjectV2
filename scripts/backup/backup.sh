#!/bin/bash

#colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# -------------- local variables -------------- #
declare -A dic_var
declare delimetr=','
dic_var['script']="no"

# -------------- functions -------------- #
fun_help()
{
    echo "Usage: `basename $0` [ h p f t ]"   
    echo " -h|--help    help."
    echo " -p|--print   print local variables [ -p ]."    
    echo " -f|--files   files for backup. [ -f 'file1.txt,file2.txt,...'] delimeter='${delimetr}'."  
    echo " -c|--create  create script for backup. [ -c 'run_back_up.sh' ]"   
    echo " -d|--destination  destination path."
    echo " -n|--name    name backup. Sample: [ -n 'backup' ]."
    echo " -s|--script  script for restore (yes/no)."
}

fun_print_local_variables()
{
    echo "delimetr='$delimetr'"
    for key in "${!dic_var[@]}"; do
        echo "$key='${dic_var[$key]}'"
    done
}

fun_set_params(){
    dic_var['date']=$(date +'%Y-%m-%d-%H-%M-%S');
    dic_var['name_backup']="${dic_var['name']}_${dic_var['date']}"
    dic_var['fullpath_backup']="${dic_var['destination']}/${dic_var['name_backup']}"    
}

# -------------- the create section ------------------------------ #

fun_create_main_script()
{    
    #file_name="create_backup.sh"
    file_name="${dic_var['create']}"    
    printf "#!/bin/bash\n" > $file_name
    printf "# Create an folder.\n" >> $file_name
    printf "mkdir '${dic_var['fullpath_backup']}'\n" >> $file_name       
    if [ -v dic_var['files'] ]; 
    then  
        ###########################################
        # copy files to the backup folder
        printf "# copy files to folder\n" >> $file_name  
        OIFS=$IFS
        IFS=${delimetr}   
        files=${dic_var['files']}            
            for f in $files
            do
                printf "cp '$f' '${dic_var['fullpath_backup']}'\n" >> $file_name                
            done
        IFS=$OIFS
        if [ "${dic_var['script']}" == "yes" ];
        then
            ###########################################
            # create script for restore
            file_name_restore="${dic_var['fullpath_backup']}/restore_${dic_var['date']}.sh"
            printf "\n\n\n############################\n" >> $file_name
            printf "# Create a restore script.\n" >> $file_name
            printf "cp /dev/null '$file_name_restore'\n" >> $file_name    
            printf "echo '#!/bin/bash' >> '$file_name_restore'\n" >> $file_name 
            OIFS=$IFS
            IFS=${delimetr}   
            files=${dic_var['files']}
                printf "# copy files to back\n" >> $file_name  
                for f in $files
                do                
                    base_name=$(basename ${f})
                    printf "echo 'cp ${dic_var['fullpath_backup']}/$base_name' '$f' >> '$file_name_restore'\n" >> $file_name  
                done
            IFS=$OIFS
        fi
    fi
    printf "\n\n\n" >> $file_name 
    printf "echo 'create: ${dic_var['fullpath_backup']}'\n" >> $file_name  
       
    #exit "somemything wrong."
    printf "${GREEN}${file_name} created.${NC}\n"
    exit 0
}
# -------------- the create section ------------------------------ #

# -------------- main -------------- #
while :;  
do  
    case $1 in  
        -h|--help) fun_help; exit 0 ;; 
        -f|--files) dic_var['files']=$2; shift ;;       
        -p|--print) dic_var['print']='1'; ;;         
        -c|--create) dic_var['create']=$2; shift ;; 
        -d|--destination) dic_var['destination']=$2; shift ;; 
        -n|--name) dic_var['name']=$2; shift ;;  
        -s|--script) dic_var['script']=$2; shift ;; 

        -?*) printf "${RED}wrong param '$1'.${NC}\n";        
             fun_help; 
             exit 1 ;;
         *) break
    esac
    shift
done

# -------------- run -------------- #

fun_set_params

if [ -v dic_var['print'] ]; 
   then fun_print_local_variables   
fi

if [ -v dic_var['create'] ]; 
    then fun_create_main_script     
fi

exit 0;