import streamlit as st
import pandas as pd
from datetime import datetime

# Sample data for rooms and bookings
rooms = {
    "Room Number": [101, 102, 103, 104, 105],
    "Type": ["Single", "Double", "Single", "Suite", "Double"],
    "Price": [100, 150, 100, 250, 150],
    "Available": [True, True, True, True, True]
}

bookings = []

# Function to check room availability
def check_availability(room_number):
    for room in rooms['Room Number']:
        if room == room_number:
            return rooms['Available'][rooms['Room Number'].index(room)]
    return False

# Function to book a room
def book_room(name, room_number, check_in, check_out):
    if check_availability(room_number):
        bookings.append({
            "Name": name,
            "Room Number": room_number,
            "Check-in": check_in,
            "Check-out": check_out
        })
        rooms['Available'][rooms['Room Number'].index(room_number)] = False
        return True
    return False

# Function to checkout
def checkout(room_number):
    for booking in bookings:
        if booking["Room Number"] == room_number:
            bookings.remove(booking)
            rooms['Available'][rooms['Room Number'].index(room_number)] = True
            return True
    return False

# Streamlit App
st.title("Hotel Management System")

menu = ["View Rooms", "Book Room", "Check Out"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "View Rooms":
    st.subheader("View Rooms")
    df_rooms = pd.DataFrame(rooms)
    st.dataframe(df_rooms)

elif choice == "Book Room":
    st.subheader("Book Room")
    name = st.text_input("Name")
    room_number = st.number_input("Room Number", min_value=min(rooms['Room Number']), max_value=max(rooms['Room Number']))
    check_in = st.date_input("Check-in Date", min_value=datetime.today())
    check_out = st.date_input("Check-out Date", min_value=check_in)

    if st.button("Book"):
        if book_room(name, room_number, check_in, check_out):
            st.success("Room booked successfully!")
        else:
            st.error("Room is not available!")

elif choice == "Check Out":
    st.subheader("Check Out")
    room_number = st.number_input("Room Number", min_value=min(rooms['Room Number']), max_value=max(rooms['Room Number']))

    if st.button("Check Out"):
        if checkout(room_number):
            st.success("Checked out successfully!")
        else:
            st.error("Room is not currently booked!")                       
