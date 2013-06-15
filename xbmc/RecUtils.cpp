#include "guilib/Key.h"
#include "RecUtils.h"
#include <stdio.h>
#include <string.h>
#define PIONEER_VOLUP "VU"
#define PIONEER_VOLDOWN "VD"

void RecUtils::doRecVolumeChange(int ActionID)
	{
		if (ActionID == ACTION_VOLUME_UP)
		{
			doRecVolumeUP();
		}
		else if (ActionID == ACTION_VOLUME_DOWN)
		{
			doRecVolumeDown();
		}
	}

void RecUtils::doRecVolumeUP()
	{
		sendCommand(PIONEER_VOLUP);
	}

void RecUtils::doRecVolumeDown()
	{
		sendCommand(PIONEER_VOLDOWN);
	}

void RecUtils::sendCommand(const char *command)
	{
		char result[100];
		strcpy(result,"python Pioneer.py ");
		strcat(result,command);
		strcat(result," &");
		FILE * f = popen( result , "r" );
    		if ( f == 0 ) {
    			fprintf( stderr, "Could not execute\n" );
    			return;
    		}
    		const int BUFSIZE = 1000;
    		char buf[ BUFSIZE ];
    		while( fgets( buf, BUFSIZE,  f ) ) {
    			//fprintf( stdout, "%s", buf  );
    		}
    		pclose( f );
	}
