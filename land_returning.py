import datetime

def return_land(land_manager, returned_customer_name, kitta_number, return_date):
    for index, land in enumerate(land_manager.land_data):
        if land['kitta_number'] == kitta_number and land['status'] == 'Not Available':
            rent_start = datetime.datetime.strptime(land['rent_start_date'], '%Y-%m-%d %H:%M:%S')
            rent_duration = (return_date - rent_start).days // 30
            fine = max(0, (rent_duration - land['area']) * land['price'])  # Calculate fine
            total_amount = land['price'] * rent_duration + fine  
            land['status'] = 'Available'
            land['rented_to'] = None  
            invoice_file = f"return_invoice_{land['kitta_number']}_{return_date.strftime('%Y%m%d%H%M%S')}.txt"
            with open(invoice_file, 'w') as file:
                file.write(f"+{'-' * 40}+\n")
                file.write(f"| {'Return Invoice'.center(38)} |\n")
                file.write(f"+{'-' * 40}+\n")
                file.write(f"| {'Return Time'.ljust(20)} | {return_date.strftime('%Y-%m-%d %H:%M:%S').ljust(22)} |\n")
                file.write(f"| {'Rent Start Time'.ljust(20)} | {rent_start.strftime('%Y-%m-%d %H:%M:%S').ljust(22)} |\n")
                file.write(f"| {'Customer Name'.ljust(20)} | {returned_customer_name.ljust(22)} |\n")
                file.write(f"| {'Kitta Number'.ljust(20)} | {str(kitta_number).ljust(22)} |\n")
                file.write(f"| {'City'.ljust(20)} | {land['city'].ljust(22)} |\n")
                file.write(f"| {'Direction'.ljust(20)} | {land['direction'].ljust(22)} |\n")
                file.write(f"| {'Return Date'.ljust(20)} | {return_date.strftime('%Y-%m-%d').ljust(22)} |\n")
                file.write(f"| {'Rent Duration'.ljust(20)} | {str(rent_duration) + ' months'.ljust(22)} |\n")
                file.write(f"| {'Area'.ljust(20)} | {str(land['area']) + ' anna'.ljust(22)} |\n")
                file.write(f"| {'Total Amount'.ljust(20)} | {str(total_amount) + ' NPR'.ljust(22)} |\n")
                if fine > 0:
                    file.write(f"| {'Fine for Late Return'.ljust(20)} | {str(fine) + ' NPR'.ljust(22)} |\n")
                file.write(f"+{'-' * 40}+\n")
            land_manager.update_land_data_file()
            print(f"Land with Kitta Number {land['kitta_number']} has been returned successfully.")
            return
    print(f"Land with Kitta Number {kitta_number} is either not rented or is not currently rented.")
