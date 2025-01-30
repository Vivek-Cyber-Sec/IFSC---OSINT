import requests
from colorama import Fore, Style

# Large ASCII Art Title for IFSC OSINT (using raw string to avoid escape warning)
def print_ascii_art():
    ascii_art = r"""
    _______________ ______   ____  _____ _____   ________
   /  _/ ____/ ___// ____/  / __ \/ ___//  _/ | / /_  __/
   / // /_   \__ \/ /      / / / /\__ \ / //  |/ / / /   
 _/ // __/  ___/ / /___   / /_/ /___/ // // /|  / / /    
/___/_/    /____/\____/   \____//____/___/_/ |_/ /_/     
    """
    print(Fore.GREEN + ascii_art + Style.RESET_ALL)
    print(Fore.MAGENTA + "                    Author: Vivek" + Style.RESET_ALL)

# Function to fetch IFSC code data
def get_ifsc_data(ifsc_code):
    url = f"https://ifsc.razorpay.com/{ifsc_code}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(Fore.RED + "Invalid IFSC code or API error!" + Style.RESET_ALL)
        return None

# Function to display the output with large and aligned text
def display_data(data):
    if data:
        print(Fore.GREEN + f"{'BANK':<20}: {data['BANK']}" + Style.RESET_ALL)
        print(Fore.YELLOW + f"{'IFSC':<20}: {data['IFSC']}" + Style.RESET_ALL)
        print(Fore.CYAN + f"{'BRANCH':<20}: {data['BRANCH']}" + Style.RESET_ALL)
        print(Fore.BLUE + f"{'ADDRESS':<20}: {data['ADDRESS']}" + Style.RESET_ALL)
        print(Fore.MAGENTA + f"{'CONTACT':<20}: {data['CONTACT']}" + Style.RESET_ALL)
        print(Fore.WHITE + f"{'CITY':<20}: {data['CITY']}" + Style.RESET_ALL)
        print(Fore.GREEN + f"{'DISTRICT':<20}: {data['DISTRICT']}" + Style.RESET_ALL)
        print(Fore.YELLOW + f"{'STATE':<20}: {data['STATE']}" + Style.RESET_ALL)
        print(Fore.CYAN + f"{'RTGS':<20}: {data['RTGS']}" + Style.RESET_ALL)
        print(Fore.BLUE + f"{'BANK CODE':<20}: {data['BANKCODE']}" + Style.RESET_ALL)

# Main function to execute the tool
def main():
    print_ascii_art()
    print(Fore.GREEN + "\nWelcome to the IFSC Lookup Tool!\n" + Style.RESET_ALL)

    # User input for IFSC code
    ifsc_code = input(Fore.CYAN + "Enter IFSC Code: " + Style.RESET_ALL)
    data = get_ifsc_data(ifsc_code)
    display_data(data)

if __name__ == "__main__":
    main()
