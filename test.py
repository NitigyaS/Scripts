import requests
import json
from email.mime.text import MIMEText
from subprocess import Popen, PIPE



def sendmail():
    message = "Google Page Test Says your Score is " + str(score)
    msg = MIMEText(message)
    msg["From"] = "score@gscore.lo"
    msg["To"] = "nitigyasharma@hotmail.com"
    msg["Subject"] = "Score of Website."
    p = Popen(["/usr/sbin/sendmail", "-t", "-oi"], stdin=PIPE)
    p.communicate(msg.as_string())

#Fetch Data from the URL
r = requests.get("https://www.googleapis.com/pagespeedonline/v2/runPagespeed?url=http%3A%2F%2Fwww.commcarehq.org")
text=""
if r.status_code == 200:
   text=json.loads(r.text)


score = text["ruleGroups"]["SPEED"]["score"]
if score < 80:
   print "Your Score is less :" , score
   sendmail()
   print "Mail Send"
else:
   print "Your Score is OK" , score

