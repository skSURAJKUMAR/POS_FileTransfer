import os
import shutil
import time
from datetime import datetime
source_Path1=r'\\192.168.85.68\ProposalFiles'
dest_path=r'E:\Pos\Input'


def copyfile(file1):
    count=1
    # print(os.listdir(dest_path))
    li=os.listdir(source_Path1)
    for file in li:
        try:
            shutil.move(source_Path1+"\\"+file, dest_path)
            file1.write(str(count)+') '+file+'-----> '+dest_path+"\n")
            print(str(count)+') '+file+'-----> '+dest_path)
            count+=1
        except Exception as e:
            print(str(e))   
            continue   
    print('Total Number of folders in path: '+str(count-1))
    file1.write('Total Number of folders in path: '+str(count-1)+"\n")


while(True):
    try:
        now = datetime.now() 
        logdate=str(now.strftime("%Y%m%d_%H%M%S"))
        log_path = r"Logs"
        if not os.path.exists(log_path):
                os.mkdir(log_path)
        completeName = log_path+"\\log_"+logdate+'.txt'
        file1 = open(completeName, "a")
        file1.write(str(now)+"\n")
        copyfile(file1)
        time.sleep(600)
        file1.close()

    except Exception as e:
        print(str(e))
        file1.write(str(e)+"\n")
        file1.close()
        continue


    