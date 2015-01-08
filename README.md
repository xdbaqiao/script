Interesting scripts.
=======
__________________
**backup_incrimentally.sh:   Backup your Subversion incrimentally**      
This script is used to backup the svn data incrimentally.
Add in 2015-01-08.


__________________
**face_zsh.sh :    Change the zsh prompt**    
        
You can select face expression from  "\>\_<", "^_^", "T\_T", "$_$", "(￣﹁￣)", "^(oo)^" randomly.                      
Have fun!
    
**Result:**     
       
       yexinjing@vipsl ~ ^_^         
       yexinjing@vipsl ~ T_T        
       yexinjing@vipsl ~ >_<         
       yexinjing@vipsl ~ ^(oo)^           
       yexinjing@vipsl ~ (￣﹁￣)       
       yexinjing@vipsl ~ $_$           
    

__________________
**ip_ping.sh :    find the useful ip-address in LAN**    
      
You can get all ip-addresses in use and the operation system information in /tmp/os.      
Need root.

**Result:**     

    ip: 219.245.64.7 is in use.
    ip: 219.245.64.9 is in use.
    ip: 219.245.64.11 is in use.
    ip: 219.245.64.41 is in use.
    

__________________
**xdPay.py :   query the network traffic of XDU**    
      
Query the network trafficof XDU. When in batch mode, the file 'account.list' is required.      
     
**Usage:**  
    
Single : `python2 xdPay.py [-u <username>] [-p <password>]`    
Batch : `python2 xdPay.py [-b]`

    Options:
      -h, --help                               show this help message and exit
      -u USERNAME, --username=USERNAME         Name of account.
      -p PASSWORD, --password=PASSWORD         Password of account.
      -b, --batch                              Whether batch or not, default false, NEED ACCOUT LIST FILE "account.list".
      
**The format of account.list:**     
    
    account1 password1    
    account2 password2    
    account3 password3    
    account4 password4    
    ...    


LICENSE       
============
               
    Copyright 2013 YeXinjing     
        
    All codes is licensed under GPLv2. 
    This means you can use those codes according to the license on a case-by-case basis.      
    However, you cannot modify it and distribute it without supplying the source.
