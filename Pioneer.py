import sys
import telnetlib
import os
import socket

HOST = "192.168.1.114"
PORT = "8102"
LOCALHOST = 'localhost'
LOCALPORT = 50000
BACKLOG = 5 
SIZE = 1024
PIDFILE = "~/.lockfile.python.vsxRemote"

class Main:

    def _pass_args_to_command_file ( self ):
    	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	s.connect((LOCALHOST,LOCALPORT)) 
	s.send(self.PARAMS) 
	data = s.recv(SIZE) 
	s.close() 
	print 'Received:', data
    def _check_lock_file ( self ):
	if os.access(os.path.expanduser(PIDFILE), os.F_OK):
        	#if the lockfile is already there then check the PID number 
        	#in the lock file
        	pidfile = open(os.path.expanduser(PIDFILE), "r")
        	pidfile.seek(0)
        	old_pd = pidfile.readline()
        	# Now we check the PID from lock file matches to the current
        	# process PID
        	if os.path.exists("/proc/%s" % old_pd):
                	print "You already have an instance of the program running"
                	print "It is running as process %s," % old_pd
			self._pass_args_to_command_file()
                	sys.exit(1)
        	else:
                	print "File is there but the program is not running"
                	print "Removing lock file for the: %s as it can be there because of the program last time it was run" % old_pd
                	os.remove(os.path.expanduser("~/.lockfile.vestibular.lock"))

	#This is part of code where we put a PID file in the lock file
	pidfile = open(os.path.expanduser(PIDFILE), "w")
	pidfile.write("%s" % os.getpid())
	pidfile.close

    def _parse_argv( self ):
        try:
            self.PARAMS = sys.argv[1]
            print "some params"
        except:
            sys.exit("no params")

    def _send_command( self ):
	LOCALHOST = ''
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	s.bind((LOCALHOST,LOCALPORT)) 
	s.listen(BACKLOG) 
	try:
            tn = telnetlib.Telnet(HOST,PORT)
            tn.write(self.PARAMS + "\r\n")
            tn.read_some()
	    while 1:
		client, address = s.accept()
		data = client.recv(SIZE)
		if data:
		    tn.write(data + "\r\n")
		    client.send(data)
            tn.close()
            print self.PARAMS
        except:
            print "Command Failed"

    def __init__( self ):
        self._parse_argv()
	self._check_lock_file()
        self._send_command()

if ( __name__ == "__main__" ):
    Main()
