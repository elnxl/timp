from pathlib import Path
import os
import argparse
import base64
import glob
from ast import literal_eval
from time import sleep

def func():
  ban_list=data
  dir_list=os.listdir()
  temp={}
  
  for name in dir_list:
    for ban in ban_list:
      if name in glob.glob(ban):
        temp[name] = oct(os.stat(name).st_mode)[-3:]
        os.chmod(name,0o700)
  
  temp['PID']=os.getpid()

  with open('temp.ini','w') as f:
    print(temp,file=f)
  os.chmod('temp.ini',0o600)

  while True:
    dir_list=os.listdir()
    for name in dir_list:
      for ban in ban_list:
        if name in glob.glob(ban) and name not in temp.keys():
          os.remove(name)
    sleep(1)


if __name__=="__main__":
  parser = argparse.ArgumentParser(description='chmod control')
  parser.add_argument('-s','--stop', help='stop running', default=False, action='store_true')
  argc=parser.parse_args()

  password=input('Please, enter the password ').encode()
  password=base64.b64encode(password)
  password=password.decode()

  data=open('template.tbl','r').read().splitlines()
  
  try:
    if not argc.stop:
      if len(data)<1:
        raise KeyError

      with open("template.tbl", "r+") as f: 
        s = f.read()
        f.seek(0); 
        f.write(password+ '\n' + s)
      os.chmod('template.tbl', 0o600)
      print('Running ...')
      func()

    else:
      if password!=data[0]:
        raise ZeroDivisionError
      
      temp_ini=open('temp.ini','r').read()
      temp_ini=literal_eval(temp_ini)
      
      try:
        os.kill(int(temp_ini['PID']),9)
        print('prog is stopped')
      except:
        print('prog is already stopped, trying to return default permissions')
        
      for name in temp_ini:
        if name!='PID':
          os.chmod(name,int(temp_ini[name],base=8))
      print('permissions are returned to default')
      os.remove('temp.ini')
      os.kill(int(temp_ini['PID']),9)  


  except KeyError:
    print('regenerate file')
  except ZeroDivisionError:
    print('incorrect password')
  except:
    print('smth goes wrong')
