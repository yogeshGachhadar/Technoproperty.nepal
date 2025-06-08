import datetime

def rent_land(land_manager, customer_name, kitta_number, duration):
    for index, land in enumerate(land_manager.land_data):
        if land['kitta_number'] == kitta_number and land['status'] == 'Available':
            land['status'] = 'Not Available'
            land['rented_to'] = customer_name
            now = datetime.datetime.now()
            rent_start_date = now.strftime('%Y-%m-%d %H:%M:%S')  
            land['rent_start_date'] = rent_start_date  
            invoice_file = f"rent_invoice_{land['kitta_number']}_{now.strftime('%Y%m%d%H%M%S')}.txt"
            with open(invoice_file, 'w') as file:
                file.write(f"Rent Start Time: {now.strftime('%Y-%m-%d %H:%M:%S')}, Return By: {(now + datetime.timedelta(days=duration * 30)).strftime('%Y-%m-%d %H:%M:%S')}\n")
                file.write(f"Rent Invoice\n")
                file.write(f"Customer Name: {customer_name}\n")
                file.write(f"Kitta Number: {land['kitta_number']}\n")
                file.write(f"City: {land['city']}\n")
                file.write(f"Direction: {land['direction']}\n")
                file.write(f"Rent Start Date: {now.strftime('%Y-%m-%d')}\n")
                file.write(f"Rent Duration: {duration} months\n")
                file.write(f"Area: {land['area']} anna\n")
                file.write(f"Total Amount: {land['price'] * duration} NPR\n")
            land_manager.update_land_data_file()
            print(f"Land with Kitta Number {land['kitta_number']} has been rented successfully.")
            return
    print(f"Land with Kitta Number {kitta_number} is not available for rent.")
