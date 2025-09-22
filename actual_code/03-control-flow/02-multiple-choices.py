print("=*=" * 20)

user_channel = input("What channel would you like to watch? ").lower().strip().replace(" ", "")

if user_channel == "bbc 1" or user_channel == "bbc1":
    print("It's the time for the news")
elif user_channel == "bbc2":  # else if  =>  elif
    print("It's time for University Challenge")
elif user_channel == "cbeebies":
    print("It's time for Bluey")
else:  # fallback -> if nothing else matches!
    print("Are you sure? Why not have a walk?")