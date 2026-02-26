import random
import time

# Accept limits
min_temp = int(input("Enter minimum temperature limit: "))
max_temp = int(input("Enter maximum temperature limit: "))
runtime = int(input("Enter total runtime (in seconds): "))

print("\nTemperature Monitoring System Started...\n")

start_time = time.time()

while True:
    current_time = time.time()
    elapsed_time = current_time - start_time

    if elapsed_time >= runtime:
        print("\n Monitoring stopped. Runtime completed.")
        break

    # Generate random temperature
    temperature = random.randint(0, 50)

    print(f"Current Temperature: {temperature}°C → ", end="")

    if temperature < min_temp:
        print(" BELOW minimum limit")
    elif temperature > max_temp:
        print("ABOVE maximum limit")
    else:
        print("NORMAL")

    time.sleep(2)
