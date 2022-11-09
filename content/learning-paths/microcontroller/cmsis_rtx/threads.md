---
# User change
title: "Create RTOS threads"

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
We shall now implement the main RTOS thread (`app_main()`), whose role is primarily to start and manage the other threads of the system.

In this example we shall create 3 threads. The number and naming of the threads is arbitrary.

## Create app_main()

Right click on the `Source` folder under the `FVP` target, and `Add a new item`. Select `C file (.c)`, and create the following `app_main.c`.

```C
// #include "RTE_Components.h"
// #include  CMSIS_device_header
#include "cmsis_os2.h"

void thread1(void *);
void thread2(void *);
void thread3(void *);

void app_main (void *argument) {
	osThreadNew(thread1, NULL, NULL);	// Create thread1
	osThreadNew(thread2, NULL, NULL);	// Create thread2
	osThreadNew(thread3, NULL, NULL);	// Create thread3
}
```
## Create threads

We can now implement the functionality of the threads themselves. Let's start with a simple basic example... each thread will endlessly say hello, and then pause for a period.

Right click on the `Source` folder under the `FVP` target, and `Add a new item`. Select `C file (.c)`, and create the following `threads.c`.
```C
#include "cmsis_os2.h"
#include <stdio.h>

void __attribute__((noreturn)) thread1(void *argument){
	for(;;){
		printf("hello from thread1\n");
		osDelay(10000);
	}
}

void __attribute__((noreturn)) thread2(void *argument){
	for(;;){
		printf("hello from thread2\n");
		osDelay(10000);
	}
}

void __attribute__((noreturn)) thread3(void *argument){
	for(;;){
		printf("hello from thread3\n");
		osDelay(10000);
	}
}
```
Note that two other threads, `osRtxIdleThread` and `osRtxTimerThread` will be automatically created.

## Build and run the example

Save all files, and `build` (`F7`) the example.

Click `Debug` (`Ctrl+F5`) to launch the FVP, and put the IDE into debug mode.
* Use the menu (`View` > `Watch Windows` > `RTX RTOS`) to observe the RTOS features.
* Use the menu (`View` > `Serial Windows` > `Debug (printf)`) to observe the printf output.

Click `Run` (`F5`) to start the application.

However... no output is seen in the `printf viewer`?

Stop the application. Observe in the `RTX RTOS` view that our threads do exist and have run.

The solution is not immediately obvious, but is a very useful one, both for the FVP and real hardware... [Event Recorder](https://www.keil.com/pack/doc/compiler/EventRecorder/html/index.html).
