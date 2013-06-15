#ifndef RECUTILS_H
#define RECUTILS_H

class RecUtils
{
public:
static void doRecVolumeChange(int ActionID);
static void doRecVolumeUP();
static void doRecVolumeDown();
static void sendCommand(const char* command);
};

#endif
