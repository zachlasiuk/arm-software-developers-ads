---
# User change
title: "Using Event Recorder"

weight: 5 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
Event Recorder provides an API for annotations in the application code or software component libraries. These annotations are stored in an `event buffer`, which can also be used for `printf()` output.

## Manage run-time environment

Open the `Manage run-time environment` dialog, and enable `Compiler` > `Event Recorder`. If using the FVP, select `Semihosting` mode. If using real hardware, select `DAP`.

Enable `Compiler` > `I/O` > `STDOUT`, and set to `EVR` (Event recorder) mode. This will redirect printf() output to the event buffer.

Click `OK` to save.

## Add Event Recorder to main

Open `main.c` in the editor. We must add a function call to initialize the event recorder. Include the header file:
```C
#include "EventRecorder.h"              // Keil.ARM Compiler::Compiler:Event Recorder
```
To the `main()` function, add this function call before `osKernelInitialize()`:
```C
	EventRecorderInitialize (EventRecordAll, 1);	// initialize and start Event Recorder
```
## Configure EventRecorder

Open the source file `Compiler` > `EventRecorderConf.h`, and click the `Configuration Wizard` tab. Set `Number of Records` to `2048`.

Save and close this file.

## Set the event buffer

Finally, edit the scatter file to locate the event buffer. Create a new execution region (after `ARM_LIB_STACK`):
```text
	EVENT_BUFFER  0x20060000 UNINIT 0x10000 {
		EventRecorder.o (+ZI)               }
```
If you get a link-time warning:
```text
Warning: L6314W: No section matches pattern EventRecorder.o(ZI).
```
Verify that `Link-time optimization` was disabled in `C/C++ (AC6)` tab in the `Target Options` dialog.

## Build and run the example

Save all files, and `build` (`F7`) the example.

Click `Debug` (`Ctrl+F5`) to launch the FVP, and put the IDE into debug mode.

Click `Run` (`F5`) to start the application.

Observer the thread output in the `printf viewer`
```
hello from thread1
hello from thread2
hello from thread3
hello from thread1
hello from thread2
hello from thread3
...
```
## Event recorder view

Use the menu (`View` > `Analysis Windows` > `Event Recorder`) to open the viewer.

Observe that printf output is in the form of the ASCII codes of the text, not very readable. To make use of this view, it is better to use EventRecorder API rather than printf statements.

## Extend example

Edit the `threads.c` file, and include the header file:
```C
#include "EventRecorder.h"
```
Add call in each thread to `EventRecord2()` with the thread number as the second parameter, for example:
```C
void __attribute__((noreturn)) thread2(void *argument){
	for(;;){
		printf("hello from thread2\n");
		EventRecord2 (1+EventLevelAPI, 2, 0);
		osDelay(10000);
	}
}
```
Save all files, and `build` (`F7`) the example.

Click `Debug` (`Ctrl+F5`) to launch the FVP, and put the IDE into debug mode.

Click `Run` (`F5`) to start the application.

Observer these events in the Event Recorder viewer.

Optionally, use the filter to hide `STDIO` events, which shall hide the printf strings.

## Component Viewer

To make these events more meaningful in the Event Recorder viewer, we can use the [Component Viewer](https://www.keil.com/pack/doc/compiler/EventRecorder/html/cv_use.html) functionality.

Create a text file (e.g. `threads.scvd`) and copy the following:
```xml
<?xml version="1.0" encoding="utf-8"?>
 
<component_viewer schemaVersion="0.1" xmlns:xs="http://www.w3.org/2001/XMLSchema-instance" xs:noNamespaceSchemaLocation="Component_Viewer.xsd">
  <component name="MyExample" version="1.0.0"/>    <!-- name and version of the component  -->
 
    <events>
      <group name="My Events Group">
         <component name="MyApp"      brief="Threads"    no="0x00" prefix="EvrNetMM_"    info="Thread example"/>
      </group>  
 
      <event id="1" level="API"   property="Thread"        value="goodbye from thread %d[val1]"     info="threads"  />
    </events>
 
</component_viewer>
```
Exit the debugger, and return to `Target Options` > `Debug` > `Models Cortex-M Debugger`, and then click on `Manage Component Viewer Description Files`.

Click `Add Component Viewer Description File`, and browse for the above. Save the settings.

Click `Debug` (`Ctrl+F5`) to launch the FVP, and put the IDE into debug mode.

Click `Run` (`F5`) to start the application.

Observer these events in the Event Recorder viewer, again filtering out `STDIO` events.

## Observe RTX events in the Event Viewer

Finally, if you wish to see RTOS events, return to the IDE, and open the `Manage run-time environment` dialog.

Enable `CMSIS` > `RTOS2 (API)` > `Keil RTX5`, but now select `Source` variant. CLick `OK` to save. Rebuild the application.

Click `Debug` (`Ctrl+F5`) to launch the FVP, and put the IDE into debug mode.

Click `Run` (`F5`) to start the application.

Observe the events in the viewer.
