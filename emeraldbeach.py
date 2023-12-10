import csv


room_rates = {'SR': 195.00, 'DR': 250.00, 'SU': 350.00}

sales_tax_rate = 0.065
occupancy_tax_rate = 0.1125

def load_data(file_path):
    data = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data


def calculate_costs(data):
    guest_list = []
    for guest_data in data:
        room_code = guest_data[0]
        num_nights = int(guest_data[1])


        if room_code in room_rates:
            room_rate = room_rates[room_code]
            subtotal = num_nights * room_rate
            sales_tax = subtotal * sales_tax_rate
            occupancy_tax = subtotal * occupancy_tax_rate
            total = subtotal + sales_tax + occupancy_tax

            guest_list.append({
                'Room Code': room_code,
                'Number of Nights': num_nights,
                'Subtotal': subtotal,
                'Sales Tax': sales_tax,
                'Occupancy Tax': occupancy_tax,
                'Total': total
            })
        else:
            print(f"Invalid room code: {room_code}")

    return guest_list

def generate_html_report(guest_list, grand_total):
    with open("emerald-web-page.html", "w") as html_file:
     
        html_file.write("<html><head><title>Emerald Beach Hotel & Resort Sales Report</title></head><body>")

        html_file.write("<style>body {background-image: url('wallpaper_em_bc.png');}</style>")
        
        html_file.write("<table border='1' align='center'>")
        
        html_file.write("<tr><th>Room Code</th><th>Number of Nights</th><th>Subtotal</th><th>Sales Tax</th><th>Occupancy Tax</th><th>Total</th></tr>")

        # Table data
        for guest in guest_list:
            html_file.write("<tr>")
            html_file.write(f"<td>{guest['Room Code']}</td>")
            html_file.write(f"<td>{guest['Number of Nights']}</td>")
            html_file.write(f"<td>${guest['Subtotal']:.2f}</td>")
            html_file.write(f"<td>${guest['Sales Tax']:.2f}</td>")
            html_file.write(f"<td>${guest['Occupancy Tax']:.2f}</td>")
            html_file.write(f"<td>${guest['Total']:.2f}</td>")
            html_file.write("</tr>")

        # Grand total row
        html_file.write(f"<tr><td colspan='6' align='right'>Grand Total: ${grand_total:.2f}</td></tr>")

        # Close HTML tags
        html_file.write("</table></body></html>")

if __name__ == "__main__":
    file_path = "emerald.csv"
    data = load_data(file_path)
    guest_list = calculate_costs(data)
    display_report(guest_list)