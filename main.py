import sys
import datetime
from read import LandManager
from land_renting import rent_land
from land_returning import return_land

def main():
    file_path = "land_data.txt"
    land_manager = LandManager(file_path)

    while True:
        print("\nOptions:")
        print("1. Read Land Data")
        print("2. Rent Land")
        print("3. Return Land")
        print("4. Exit Program")

        choice = input("Enter your choice: ")

        if choice == '1':
            land_manager.display_land_availability()
        elif choice == '2':
            customer_name = input("Enter the customer name: ")
            kitta_number = int(input("Enter the kitta number of the land to rent: "))
            #duration = int(input("Enter the duration of the rent (in months): "))
            while True:
                duration = int(input("Enter the duration of the rent (in months): "))
                if duration<0:
                    print("It is neg input")
                else:
                    break
            rent_land(land_manager, customer_name, kitta_number, duration)
        elif choice == '3':
            customer_name = input("Enter the customer name: ")
            kitta_number = int(input("Enter the kitta number of the land to return: "))
            return_date = datetime.datetime.strptime(input("Enter the return date (YYYY-MM-DD HH:MM:SS): "), '%Y-%m-%d %H:%M:%S')
            return_land(land_manager, customer_name, kitta_number, return_date)
        elif choice == '4':
            print("Exiting program...")
            sys.exit()
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
