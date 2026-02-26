# Temperature-Monitoring-System_AnushkaSrivastava_202501100700039

## Problem Statement
To design a Python program that simulates an IoT temperature monitoring system.
The system generates temperature values at fixed intervals and displays alerts
based on minimum and maximum temperature limits for a specified runtime.

## Approach
- User inputs minimum and maximum temperature limits
- User inputs total runtime in seconds
- Random temperature values are generated every 2 seconds
- Temperature is compared with limits to display alerts
- Program stops automatically after runtime completion


## Sample Output
Enter minimum temperature limit: 20
Enter maximum temperature limit: 30
Enter total runtime (in seconds): 10
Current Temperature: 50°C → ABOVE maximum limit
Current Temperature: 18°C →  BELOW minimum limit
Current Temperature: 28°C → NORMAL
Current Temperature: 30°C → NORMAL
Current Temperature: 7°C →  BELOW minimum limit

 Monitoring stopped. Runtime completed.
