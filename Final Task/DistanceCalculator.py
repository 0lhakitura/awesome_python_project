import sqlite3
from geopy.distance import great_circle



def create_database():
    conn = sqlite3.connect('city_coordinates.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cities (
            name TEXT PRIMARY KEY,
            latitude REAL,
            longitude REAL
        )
    ''')
    conn.commit()
    conn.close()



def get_city_coordinates(city_name):
    conn = sqlite3.connect('city_coordinates.db')
    cursor = conn.cursor()

    cursor.execute('SELECT latitude, longitude FROM cities WHERE name=?', (city_name,))
    row = cursor.fetchone()

    if row:
        return row
    else:
        print(f"City coordinates for {city_name} not found.")
        latitude = float(input("Enter the latitude for the city: "))
        longitude = float(input("Enter the longitude for the city: "))
        cursor.execute('INSERT INTO cities (name, latitude, longitude) VALUES (?, ?, ?)',
                       (city_name, latitude, longitude))
        conn.commit()
        return latitude, longitude



def calculate_distance(city1, city2):
    coords1 = get_city_coordinates(city1)
    coords2 = get_city_coordinates(city2)

    location1 = (coords1[0], coords1[1])
    location2 = (coords2[0], coords2[1])

    distance = great_circle(location1, location2).kilometers
    return distance


if __name__ == "__main__":
    create_database()

    while True:
        city1 = input("Enter the first city: ").strip()
        city2 = input("Enter the second city: ").strip()

        distance = calculate_distance(city1, city2)
        print(f"The straight-line distance between {city1} and {city2} is approximately {distance:.2f} kilometers.")

    conn = sqlite3.connect('city_coordinates.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM cities''')
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    conn.close()