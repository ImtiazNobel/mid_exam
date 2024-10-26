class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)


class Hall:
    def __init__(self, rows, cols, hall_no):
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats = {}
        self.show_list = []

    def entry_show(self, show_id, movie_name, time):
        if show_id in self.seats:
            print(f"Show with ID {show_id} already exists.")
            return
        show_tuple = (show_id, movie_name, time)
        self.show_list.append(show_tuple)
        self.seats[show_id] = [['free' for _ in range(self.cols)] for _ in range(self.rows)]

    def book_seats(self, show_id, seats):
        if show_id not in self.seats:
            print(f"Show with ID {show_id} does not exist.")
            return
        for row, col in seats:
            if row >= self.rows or col >= self.cols or row < 0 or col < 0:
                print(f"Seat ({row}, {col}) is invalid.")
                continue
            if self.seats[show_id][row][col] == 'booked':
                print(f"Seat ({row}, {col}) is already booked.")
                continue
            self.seats[show_id][row][col] = 'booked'

    def view_show_list(self):
        if not self.show_list:
            print("No shows available.")
            return
        for show in self.show_list:
            print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, show_id):
        if show_id not in self.seats:
            print(f"Show with ID {show_id} does not exist.")
            return
        available = False
        for row in range(self.rows):
            for col in range(self.cols):
                if self.seats[show_id][row][col] == 'free':
                    print(f"Seat ({row}, {col}) is available.")
                    available = True
        if not available:
            print("No more available seats.")


run = True
star_cinema = Star_Cinema()

while run:
    print("\nOptions:")
    print("1: Add a new hall")
    print("2: Add a show to a hall")
    print("3: View all shows")
    print("4: View available seats for a show")
    print("5: Book seats")
    print("6: Exit")

    choice = int(input("\nWhich option do you want to choose? "))

    if choice == 1:
        rows = int(input("\tEnter number of rows: "))
        cols = int(input("\tEnter number of columns: "))
        hall_no = int(input("\tEnter hall number: "))
        hall = Hall(rows, cols, hall_no)
        star_cinema.entry_hall(hall)
        print("\tHall added successfully!")

    elif choice == 2:  
        hall_no = int(input("\tEnter hall number: "))
        show_id = input("\tEnter show ID: ")  
        movie_name = input("\tEnter movie name: ")
        time = input("\tEnter show time: ")
        for hall in star_cinema.hall_list:
            if hall.hall_no == hall_no:
                hall.entry_show(show_id, movie_name, time)
                print(f"\tShow '{movie_name}' added to Hall {hall_no}.")
                break
        else:
            print("\tHall not found!")

    elif choice == 3:  
        for hall in star_cinema.hall_list:
            hall.view_show_list()

    elif choice == 4:  
        hall_no = int(input("\tEnter hall number: "))
        show_id = input("\tEnter show ID: ")
        for hall in star_cinema.hall_list:
            if hall.hall_no == hall_no:
                hall.view_available_seats(show_id)
                break
        else:
            print("\tHall not found!")

    elif choice == 5: 
        hall_no = int(input("\tEnter hall number: "))
        show_id = input("\tEnter show ID: ")
        seats = input("\tEnter seats (e.g., 0,0 0,1): ").split()
        seat_list = [tuple(map(int, seat.split(','))) for seat in seats]
        for hall in star_cinema.hall_list:
            if hall.hall_no == hall_no:
                hall.book_seats(show_id, seat_list)
                break
        else:
            print("\tHall not found!")

    elif choice == 6:
        run = False

    else:
        print("Invalid option, please try again.")
