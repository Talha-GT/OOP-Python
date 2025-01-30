# 1
class StarCinema:
    halls = []
    
    @classmethod
    def add_hall(cls, hall):
        cls.halls.append(hall)

# 2. 
class Hall:
    def __init__(self, rows, cols, hall_no):
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.shows = {}
        StarCinema.add_hall(self)
    
    # 3. Method to add a show
    def add_show(self, show_id, movie_name, time):
        self.shows[show_id] = {
            "movie": movie_name,
            "time": time,
            "seats": [[0] * self.cols for _ in range(self.rows)]
        }
    
    # 4
    def book_seat(self, show_id, row, col):
        if show_id in self.shows and 0 <= row < self.rows and 0 <= col < self.cols:
            if self.shows[show_id]["seats"][row][col] == 0:
                self.shows[show_id]["seats"][row][col] = 1
                print("Seat booked successfully.")
            else:
                print("Seat already booked.")
        else:
            print("Invalid show ID or seat position.")
    
    # 5. 
    def view_shows(self):
        for show_id, details in self.shows.items():
            print(f"ID: {show_id}, Movie: {details['movie']}, Time: {details['time']}")
    
    # 6. 
    def view_available_seats(self, show_id):
        if show_id in self.shows:
            for r, row in enumerate(self.shows[show_id]["seats"]):
                for c, seat in enumerate(row):
                    if seat == 0:
                        print(f"Available: ({r}, {c})")
        else:
            print("Invalid show ID.")

#7
class CinemaCounter:
    @staticmethod
    def view_running_shows():
        for hall in StarCinema.halls:
            hall.view_shows()

    @staticmethod
    def check_available_seats(show_id):
        for hall in StarCinema.halls:
            hall.view_available_seats(show_id)

    @staticmethod
    def book_ticket(show_id, row, col):
        for hall in StarCinema.halls:
            hall.book_seat(show_id, row, col)


#8
class Hall:
    def __init__(self, rows, cols, hall_no):
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.shows = {}  # Dictionary to store show details
        StarCinema.add_hall(self)

    def add_show(self, show_id, movie_name, time):
        if show_id in self.shows:
            print("Error: Show ID already exists.")
            return
        self.shows[show_id] = {
            "movie": movie_name,
            "time": time,
            "seats": [[0] * self.cols for _ in range(self.rows)]  # 2D list for seats
        }

    def book_seat(self, show_id, row, col):
        if show_id not in self.shows:
            print("Error: Invalid show ID.")
            return
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            print("Error: Invalid seat position.")
            return
        if self.shows[show_id]["seats"][row][col] == 1:
            print("Error: Seat already booked.")
            return
        self.shows[show_id]["seats"][row][col] = 1
        print("Seat booked successfully.")


#9
class Hall:
    def __init__(self, rows, cols, hall_no):
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.__shows = {}
        StarCinema.add_hall(self)

    def add_show(self, show_id, movie_name, time):
        self.__shows[show_id] = {
            "movie": movie_name,
            "time": time,
            "seats": [[0] * self.__cols for _ in range(self.__rows)]
        }

    def view_shows(self):
        for show_id, details in self.__shows.items():
            print(f"ID: {show_id}, Movie: {details['movie']}, Time: {details['time']}")

    def view_available_seats(self, show_id):
        if show_id in self.__shows:
            for r, row in enumerate(self.__shows[show_id]["seats"]):
                for c, seat in enumerate(row):
                    if seat == 0:
                        print(f"Available: ({r}, {c})")
        else:
            print("Invalid show ID.")
