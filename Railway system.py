class Passenger:
    def __init__(self, name, source, date, destination):
        self.name = name
        self.source = source
        self.date = date
        self.destination = destination

class Ticket(Passenger):
    def __init__(self, name, source, date, destination, booking_details, price):
        super().__init__(name, source, date, destination)
        self.booking_details = booking_details
        self.price = price

    def display_details(self):
        print("Ticket Details:")
        print("Passenger Name:", self.name)
        print("Booking Details:", self.booking_details)
        print("Date:", self.date)
        print("Destination:", self.destination)
        print("Price:", self.price)

def write_to_file(ticket):
    with open("ticket_details.txt", "a") as file:
        file.write(f"Passenger Name: {ticket.name}\n")
        file.write(f"Booking Details: {ticket.booking_details}\n")
        file.write(f"Date: {ticket.date}\n")
        file.write(f"Destination: {ticket.destination}\n")
        file.write(f"Price: {ticket.price}\n\n")

def main():
    try:
        passenger_name = input("Enter passenger name: ")
        source = input("Enter source: ")
        date = input("Enter date (YYYY-MM-DD): ")
        destination = input("Enter destination: ")
        booking_details = input("Enter booking details: ")
        price = float(input("Enter ticket price: "))

        ticket = Ticket(passenger_name, source, date, destination, booking_details, price)
        ticket.display_details()

        # Write ticket details to file
        write_to_file(ticket)
        print("Ticket details written to file.")

    except ValueError:
        print("Invalid input. Please enter a valid price.")

    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()
