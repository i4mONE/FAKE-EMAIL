o
    ??c
  ?                   @   sd   d dl Z d dlZd dlZd dlZe?d?d Zd dlmZ e ?? Z	e
d? dd? Zdd	? Ze?  dS )
?    N?   ?   )?generate_user_agentu  
      __      _ 
     / _|    | |    By WHOAMI-XD
    | |_ __ _| | _____
    |  _/ _` | |/ / _ \ ┌─┐┌┬┐┌─┐┬┬
    | || (_| |   <  __/ ├┤ │││├─┤││
    |_| \__,_|_|\_\___| └─┘┴ ┴┴ ┴┴┴─
          Create fake emailc                  C   s`  	 d} dt  d t }z?t?d? t?|?}|?? d |  d }|?d?dkr0td	? td
? nZd|j	v r`|?? d |  d }|?? d |  d }td| ? td| ? td| ? td? n*d|v r|?? d |  d }td| ? td| ? td? ntd? t
d? t?  W n# ty?   td? t
d? t?  Y n ty?   td? t?  Y nw q)NTr   z3https://10minutemail.net/address.api.php?sessionid=z&_=?   Z	mail_list?subjectzHi, Welcome to 10 Minute Mailz[!] No messages yet u@    ━━━━━━━━━━━━━━━━━━━━━z"from"?from?datetimezFrom email: zdata time: zNew messages : u[    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━z
"datetime"z[*] Email expired ..? Zsorry)?sisn?tim?time?sleep?r?get?json?find?print?text?input?exit?	TypeError?AttributeError)ZERRZurlCODZsend2?msgZemlZTM? r   ?/sdcard/fakemail/FAKE-EMAIL.py?CODE   sF   





?

??r   c                  C   s?   d} dt t? ddddddd	d
?
}tj| |d?}t|?? d ?}t|?? d ?at|?? d ?atd? td| d ? td? t	?
d? t?  d S )Nz)https://10minutemail.net/address.api.php?z10minutemail.netzapplication/json,zen-US,en;q=0.5zgzip,ZXMLHttpRequestz#https://10minutemail.net/m/?lang=arZtrailers?close)
ZHostZCookiez
User-AgentZAcceptzAccept-LanguagezAccept-EncodingzX-Requested-WithZRefererZTeZ
Connection)?headersZmail_get_mailZ
session_idZmail_get_timeu\     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━z   [$] Email: ? u]     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
?   )?Coker   r   r   ?strr   r
   r   r   r   r   r   )Zvv1ckr   ?sendZemailr   r   r   ?EmAIl0   s*   ?

r#   )ZrequestsZsecretsr   r   Z	token_hexr    Z
user_agentr   Zsessionr   r   r   r#   r   r   r   r   ?<module>   s     #
