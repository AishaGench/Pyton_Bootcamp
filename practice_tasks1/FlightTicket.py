"""
2. create a python file named FlightTicket, and declare the following variables:
                1. from
                2. to
                3. ticketPrice

    use concatenation to display the full info of the ticket

    ex:
            Given Data:
                from = "Las Vegas"
                to = "McLean"
                ticket_price = 425.5

            Output:
                From Las Vegas to McLean is $425.5
"""

# Flight ticket information variables
location = "Las Vegas"
destination = "McLean"
ticket_price = 425.5

print("From " + location + " to " + destination + " is $" + str(ticket_price))