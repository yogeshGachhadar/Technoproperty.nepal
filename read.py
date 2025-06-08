import os

class LandManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.land_data = self.read_land_data()

    def read_land_data(self):
        land_data = []
        try:
            with open(self.file_path, 'r') as file:
                for line in file:
                    fields = line.strip().split(',')
                    land_info = {
                        'kitta_number': int(fields[0]),
                        'city': fields[1].strip(),
                        'direction': fields[2].strip(),
                        'area': float(fields[3]),  
                        'price': float(fields[4]),  
                        'status': fields[5].strip(),
                        'rented_to': None  
                    }
                    land_data.append(land_info)
        except FileNotFoundError:
            print(f"Error: {self.file_path} not found.")
        return land_data

    def update_land_data_file(self):
        try:
            with open(self.file_path, 'w') as file:
                for land in self.land_data:
                    line = f"{land['kitta_number']},{land['city']},{land['direction']},{land['area']},{land['price']},{land['status']},{land['rented_to']}"
                    file.write(line + '\n')
        except FileNotFoundError:
            print(f"Error: {self.file_path} not found.")

    def display_land_availability(self):
        kitta_width = 14
        city_width = 16
        direction_width = 11
        area_width = 14
        price_width = 12
        status_width = 12

        print("+" + "-" * (kitta_width + 2) + "+" + "-" * (city_width + 2) + "+" + "-" * (direction_width + 2) + "+" + "-" * (area_width + 2) + "+" + "-" * (price_width + 2) + "+" + "-" * (status_width + 2) + "+")
        print(f"| {'Kitta Num'.ljust(kitta_width)} | {'City'.ljust(city_width)} | {'Direction'.ljust(direction_width)} | {'Area (anna)'.ljust(area_width)} | {'Price'.ljust(price_width)} | {'Status'.ljust(status_width)} |")
        print("+" + "-" * (kitta_width + 2) + "+" + "-" * (city_width + 2) + "+" + "-" * (direction_width + 2) + "+" + "-" * (area_width + 2) + "+" + "-" * (price_width + 2) + "+" + "-" * (status_width + 2) + "+")

        for land in self.land_data:
            formatted_area = "{:.1f}".format(land['area'])
            if land['status'] == 'Not Available':
                status = 'Rented'
            else:
                status = land['status']
            print(f"| {str(land['kitta_number']).ljust(kitta_width)} | {land['city'].ljust(city_width)} | {land['direction'].ljust(direction_width)} | {formatted_area.ljust(area_width)} | {str(land['price']).ljust(price_width)} | {status.ljust(status_width)} |")
            print("+" + "-" * (kitta_width + 2) + "+" + "-" * (city_width + 2) + "+" + "-" * (direction_width + 2) + "+" + "-" * (area_width + 2) + "+" + "-" * (price_width + 2) + "+" + "-" * (status_width + 2) + "+")
