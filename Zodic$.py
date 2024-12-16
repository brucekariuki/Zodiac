from datetime import datetime
import random
from colorama import Fore, Style
import sys
import time
# Smooth printing for animations
def smooth_print(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Introductory ASCII art
def print_intro():
    art = r"""
             _        _        _        
            /\ (_)  /\  (_)  /\  (_)  /\   
           /  \ _   \ \  _   \ \  _   \ \  
          / /\ \ |   > \| |   > \| |   > \ 
          \/__\_\|  /_/|_|  /_/|_|  /_/|_|

                    A S T R O M E
                BY: Mistah_Cipher
    """

    smooth_print(Fore.CYAN + art + Style.RESET_ALL, delay=0.02)
    smooth_print("Welcome to AstroMe! Your zodiac and astrology assistant!", delay=0.02)
    smooth_print("Let’s uncover the mysteries of your zodiac sign!", delay=0.03)
#loading bar
def loading_bar(duration=3, bar_length=30):
    """
    Displays a loading bar animation.
    
    Args:
        duration (int): Total time in seconds for the loading animation.
        bar_length (int): The length of the loading bar.
    """
    for i in range(bar_length + 1):
        time.sleep(duration / bar_length)
        progress = "#" * i
        remaining = "-" * (bar_length - i)
        sys.stdout.write(f"\rAnalysing: [{progress}{remaining}] {int((i / bar_length) * 100)}%")
        sys.stdout.flush()
    print("\nAnalysis complete!")
# Zodiac signs and their characteristics
zodiac_info = {
    "Aries": "Adventurous, energetic, courageous, confident.",
    "Taurus": "Reliable, patient, practical, devoted.",
    "Gemini": "Versatile, curious, communicative, intelligent.",
    "Cancer": "Loyal, emotional, sympathetic, persuasive.",
    "Leo": "Creative, passionate, generous, warm-hearted.",
    "Virgo": "Analytical, hardworking, kind, practical.",
    "Libra": "Diplomatic, charming, fair-minded, social.",
    "Scorpio": "Resourceful, brave, passionate, stubborn.",
    "Sagittarius": "Optimistic, freedom-loving, humorous, philosophical.",
    "Capricorn": "Disciplined, responsible, ambitious, self-controlled.",
    "Aquarius": "Independent, creative, progressive, humanitarian.",
    "Pisces": "Compassionate, artistic, intuitive, gentle."
}

# Zodiac ASCII art
zodiac_art = {
    "Aries": r"""
                                 ♈
b                               \    /\
                                  )  ( ')
                                  (  /  )
                                   \(__)|
                                        
                                ARIES
    """,
    "Taurus": r"""
                            ♉
                                .--.
                               (    )
                               .-'-'-. 
                             /       \
                            |         |
                            \       /
                             `-._.-'
                                  
                           TAURUS
    """,
    "Gemini": r"""
                            ♊
                             .--.
                            |o_o |
                            |:_/ |
                           //   \ \
                          (|     | )
                         /'\_   _/`\
                        \___)=(___/
             
                        GEMINI
    """,
    "Cancer": r"""
                           ♋
                              _.-.  
                           .`     `.
                          /         \
                          |           |
                          \         /
                           `-.___.-`
                           
                            CANCER
    """,
    "Leo": r"""
                      ♌
                            .     .
                          _|_____|_
                            |         |
                           |  (o o)  |
                            \   -   /
                             `.___.'
                                  
                          LEO
    """,
    "Virgo": r"""
                            ♍
                             .--.
                           |o_o |
                            |:_/ |
                          //   \ \
                          (|     | )
                         /'\_   _/`\
                       \___)=(___/
                              
                           VIRGO
    """,
    "Libra": r"""
                            ♎
                             .--.
                            |    |
                            |    |
                             '--'
                                  
                           LIBRA
    """,
    "Scorpio": r"""
                            ♏
                              ,     ,
                            /(     )\\
                           (  \   /  )
                            \  \_/  /
                             \     /
                              `---`
                                   
                          SCORPIO
    """,
    "Sagittarius": r"""
                            ♐
                                \\
                             (o>
                          \\_//)
                           \_/_)
                            _|_ 
                                 
                           SAGITTARIUS
    """,
    "Capricorn": r"""
                            ♑
                              .      .
                            /        \
                           |          |
                            \        /
                             `-.__.-'
                                  
                           CAPRICORN
    """,
    "Aquarius": r"""
                            ♒
                              .-.
                            |   |
                            |   |
                             `-'
                                  
                             AQUARIUS
    """,
    "Pisces": r"""
                           ♓
                             \    /
                              )  (
                             (    )
                             \__/
                                   
                           PISCES
    """
}

# Zodiac greetings
zodiac_greetings = {
    "Aries": "Today is your day to take bold actions!",
    "Taurus": "Remember to enjoy life's little pleasures today.",
    "Gemini": "Communication is your superpower—use it wisely.",
    "Cancer": "Focus on self-care and emotional balance today.",
    "Leo": "Shine bright! Your charisma can light up any room.",
    "Virgo": "Stay organized and take small steps toward your goals.",
    "Libra": "Balance is key—focus on relationships today.",
    "Scorpio": "Trust your instincts; they're your secret weapon.",
    "Sagittarius": "Adventure awaits! Don't hold back today.",
    "Capricorn": "Hard work will pay off—keep pushing forward.",
    "Aquarius": "Your innovative ideas can make a big difference.",
    "Pisces": "Dream big! Your creativity knows no bounds."
}

# Zodiac compatibility
zodiac_compatibility = {
    "Aries": ["Leo", "Sagittarius", "Aquarius"],
    "Taurus": ["Virgo", "Capricorn", "Cancer"],
    "Gemini": ["Libra", "Aquarius", "Aries"],
    "Cancer": ["Pisces", "Scorpio", "Taurus"],
    "Leo": ["Aries", "Sagittarius", "Gemini"],
    "Virgo": ["Taurus", "Capricorn", "Scorpio"],
    "Libra": ["Gemini", "Aquarius", "Leo"],
    "Scorpio": ["Cancer", "Pisces", "Virgo"],
    "Sagittarius": ["Leo", "Aries", "Aquarius"],
    "Capricorn": ["Taurus", "Virgo", "Pisces"],
    "Aquarius": ["Gemini", "Libra", "Sagittarius"],
    "Pisces": ["Cancer", "Scorpio", "Capricorn"]
}

# Determine zodiac sign based on date of birth
def get_zodiac_sign(day, month):
    zodiac_dates = [
        (20, "Capricorn", "Aquarius"), (19, "Aquarius", "Pisces"), (20, "Pisces", "Aries"),
        (20, "Aries", "Taurus"), (21, "Taurus", "Gemini"), (21, "Gemini", "Cancer"),
        (22, "Cancer", "Leo"), (22, "Leo", "Virgo"), (23, "Virgo", "Libra"),
        (23, "Libra", "Scorpio"), (22, "Scorpio", "Sagittarius"), (21, "Sagittarius", "Capricorn")
    ]
    if day > zodiac_dates[month - 1][0]:
        return zodiac_dates[month - 1][2]
    return zodiac_dates[month - 1][1]

# Function to get valid input with retry mechanism
def get_valid_input(prompt, valid_inputs, retries=3):
    for attempt in range(retries):
        user_input = input(prompt).strip().lower()  # Convert to lowercase for consistency
        if user_input in valid_inputs:
            return user_input.capitalize()  # Make it sentence case
        else:
            print(f"Invalid input. You have {retries - attempt - 1} attempts left.")
    print(f"Too many invalid attempts for {prompt}. Restarting the program.")
    sys.exit()  # Exit the program after retry limit is reached

# Function to validate numeric input for day, month, or year
def get_valid_numeric_input(prompt, min_value, max_value, retries=3):
    for attempt in range(retries):
        try:
            user_input = int(input(prompt).strip())
            if min_value <= user_input <= max_value:
                return user_input
            else:
                print(f"Invalid input. {prompt} should be between {min_value} and {max_value}.")
        except ValueError:
            print(f"Invalid input. {prompt} should be a number.")
        
        print(f"You have {retries - attempt - 1} attempts left.")
    print(f"Too many invalid attempts for {prompt}. Restarting the program.")
    sys.exit()  # Exit the program after retry limit is reached

# Function for smooth transition printing
def smooth_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
print_intro()
# Introductory message with transition
smooth_print(Fore.CYAN + "Welcome to AstroMe! ✨ Your personalized zodiac and astrology assistant!" + Style.RESET_ALL)
smooth_print(Fore.YELLOW + "I will give you details about your zodiac sign, age, and more!" + Style.RESET_ALL)

# Input Fields with Independent Validation

name = input("Enter your name: ").strip().capitalize()  # Name in sentence case
pronoun = get_valid_input("Enter your pronoun (he/she/they): ", ["he", "she", "they"])
day = get_valid_numeric_input("Day of birth (1-31): ", 1, 31)
month = get_valid_numeric_input("Month of birth (1-12): ", 1, 12)
year = get_valid_numeric_input("Year of birth (e.g., 2000): ", 1900, 2024)
#loading
# ASCII art for AstroMe intro

# Call the loading bar here
loading_bar()
# Calculate age
today = datetime.today()
dob = datetime(year, month, day)
age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

# Calculate days until next birthday
next_birthday = dob.replace(year=today.year)
if next_birthday < today:
    next_birthday = next_birthday.replace(year=today.year + 1)
days_to_birthday = (next_birthday - today).days

# Get zodiac sign and characteristics
zodiac_sign = get_zodiac_sign(day, month)
characteristics = zodiac_info[zodiac_sign]

# Lucky number
lucky_number = random.randint(1, 100)

# Output with transition for each line
print("___________________________________________________")
smooth_print(Fore.CYAN + f"\nName: {name}" + Style.RESET_ALL)
smooth_print(Fore.YELLOW + f"Age: {age} years old." + Style.RESET_ALL)
smooth_print(Fore.GREEN + f"Happy_Birthday_in {days_to_birthday} days." + Style.RESET_ALL)
smooth_print(Fore.MAGENTA + f"zodiac sign is {zodiac_sign}.\n" + Style.RESET_ALL)
smooth_print(Fore.BLUE + f"{zodiac_art[zodiac_sign]}" + Style.RESET_ALL)
smooth_print(Fore.RED + f"Characteristics: {characteristics}" + Style.RESET_ALL)
smooth_print(Fore.CYAN + f"Special Message: {zodiac_greetings[zodiac_sign]}" + Style.RESET_ALL)
smooth_print(Fore.GREEN + f"Compatible Zodiac Signs: {', '.join(zodiac_compatibility[zodiac_sign])}" + Style.RESET_ALL)
smooth_print(Fore.YELLOW + f"Lucky Number: {lucky_number}" + Style.RESET_ALL)