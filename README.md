# IFSC OSINT

**IFSC OSINT** is a simple Python tool that allows you to fetch and display bank information based on the IFSC code. It uses the **Razorpay IFSC API** to retrieve the data and provides the details in a clean, colorful format on the terminal.

### Features:
- Fetches details about the bank, branch, address, contact, city, state, etc., for any given IFSC code.
- Provides a colorful, easy-to-read output using the `colorama` library.
- The tool includes an ASCII art title to make it visually appealing.

### Requirements:
- **Python 3.x**
- **requests**: For making HTTP requests to the Razorpay IFSC API.
- **colorama**: For color formatting in the terminal output.

### Installation:

1. **Clone this repository** or download the `ifsc.py` file.

2. **Install the required libraries** by running the following command:

   ```bash
   pip install requests colorama
   ```

3. **Run the script**:

   Navigate to the folder where the script is saved and run it:

   ```bash
   python ifsc.py
   ```

### Usage:

Once you run the script, you will be prompted to enter an IFSC code. After you input the code, the tool will fetch the corresponding bank details and display them in the following format:

```
  IFSC OSINT

                    Author: Vivek

Welcome to the IFSC Lookup Tool!

Enter IFSC Code: HDFC0CAGSBK
BANK: HDFC BANK
IFSC: HDFC0CAGSBK
BRANCH: THE AGS EMPLOYEES' CO-OP BANK LTD
ADDRESS: PARK HOUSE ROAD, BANGALORE 560001
CONTACT: 2265658
CITY: BANGALORE
DISTRICT: BANGALORE URBAN
STATE: KARNATAKA
RTGS: True
BANK CODE: HDFC
```

### Output:
The tool will show the following information (depending on the IFSC code):
- **BANK**: The name of the bank
- **IFSC**: The IFSC code you provided
- **BRANCH**: The bank branch name
- **ADDRESS**: Address of the branch
- **CONTACT**: Contact number
- **CITY**: The city where the branch is located
- **DISTRICT**: The district of the branch
- **STATE**: The state of the branch
- **RTGS**: Whether the branch supports RTGS
- **BANK CODE**: The bank code

### Example:
```
    _______________ ______   ____  _____ _____   ________
   /  _/ ____/ ___// ____/  / __ \/ ___//  _/ | / /_  __/
   / // /_   \__ \/ /      / / / /\__ \ / //  |/ / / /   
 _/ // __/  ___/ / /___   / /_/ /___/ // // /|  / / /    
/___/_/    /____/\____/   \____//____/___/_/ |_/ /_/     
 
                    Subtitle: Vivek

Welcome to the IFSC Lookup Tool!

Enter IFSC Code: HDFC0CAGSBK
BANK: HDFC BANK
IFSC: HDFC0CAGSBK
BRANCH: THE AGS EMPLOYEES' CO-OP BANK LTD
ADDRESS: PARK HOUSE ROAD, BANGALORE 560001
CONTACT: 2265658
CITY: BANGALORE
DISTRICT: BANGALORE URBAN
STATE: KARNATAKA
RTGS: True
BANK CODE: HDFC
```

### Troubleshooting:
- Ensure that you are connected to the internet as the tool fetches data from an external API.
- If you encounter any errors related to missing libraries, make sure you have installed all dependencies using `pip install`.

### License:
This project is open-source and available under the MIT License.
