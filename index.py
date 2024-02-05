import time

def get_positive_integer_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            user_value = int(user_input)
            if user_value <= 0:
                print("Please enter a positive integer.")
            else:
                return user_value
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

my_timer = get_positive_integer_input("Enter the time in seconds: ")

while my_timer > 0:
    hours = my_timer // 3600
    remaining_seconds = my_timer % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60

    print(f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}")
    time.sleep(1)
    my_timer -= 1

print("Boom!")
