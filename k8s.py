Code present in cg-bin:
 
--------------------------------------------------------------------------------------------------------------
  
#!/usr/bin/python3

import subprocess
import cgi


print("Content-Type: text/html")
print()

f = cgi.FieldStorage()
cmd = f.getvalue("x")
result = subprocess.getoutput(cmd)
print(result)
