import sys
def main():
    """
    The main script funtion.
    We get the user data and combine it to make a new key in the dictionary [band_name]
    we then exit with a success exit code.

    :return:
    """

    # Initialise the empty band dictionary
    band_dict = {}

    # Call the user prompt function
    prompt_details(band_dict)

    # Format the band name and add it to the dictionary
    band_dict['band_name'] = f"{band_dict['home_city']} {band_dict['pet_name']}"

    # Print the band na,e in quotes.
    print(f" The band name is \"{band_dict['band_name'].capitalize()}\"")

    # Exit with success (0)
    sys.exit(0)

def prompt_details(band_dict):
    """
    Prompt the user on the command line to enter some personal information
    :return:
    """

    # Prompt the user for their home city.
    band_dict['home_city'] = input("Please enter your home city: ").lower()

    # Prompt the user for their first pets name.
    band_dict['pet_name'] = input("Please enter your first pets name: ").lower()

if __name__ == '__main__':
    main()