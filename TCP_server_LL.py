import socket
import csv
import pandas as pd
import time

# AF_INET tells us IPv4 Address, SOCK_STREAM tells us TCP connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
hostName = "0.0.0.0"                                   # Use a generic host name 'open listening'
portNumber = 7001                                      # Allocate a port number to use
s.bind((hostName, portNumber))
s.listen(5)  # Leaving a queue of 5, just in case lots of inputs come in

print("Server Listening.....")

while True:                              # While the socket is open...
    clientsocket, address = s.accept()   # Create the Connection to the Client,

    # Address the Client to ensure connection
    print(f"Connection from {address} has been established.")
    clientsocket.send(bytes("Welcome to the Server", "utf-8"))

    # Establish the directory so the code is always grabbing from the current output file in the export folder
    directory = 'C:\\Users\\Owner\\AppData\\Roaming\\flightgear.org\\Export\\'

    # While we want to collect data from FlightGear (FG is running..)
    while True:
        # Open the csvfile, grab the last row, and send it to the client.
        with open(directory + 'FlightLog_Waypoints.csv', newline='') as csvfile:
            data = csvfile.readlines()
            lastRow = data[-1]
            print("This should be the most recent row of data:", lastRow)
            clientsocket.send(bytes(str(lastRow), "utf-8"))  # Send the last row of the csvfile
        # Close the csvfile to allow for data to update.
        csvfile.close()
        time.sleep(5)



    # When you no longer want to collect data
    print("Done Sending")
    clientsocket.close()   # End the connection with client
    break                  # End the while loop for the connection
s.close()                  # Close this server


# COMMENTED SECTION CAME RIGHT AFTER CLIENTSOCKET.SEND(.....)
# for row in reader:                          # For each row within the csv file
#     single_row = str(', '.join(row))        # Create a single row of data as 1 item
#     print(single_row)
#     clientsocket.send(bytes(str(single_row), "utf-8"))      # Send a single row to the client
#     # delete stuff


# reader = csv.reader(csvfile, delimiter=',', quotechar='"')    # Reader is an object that will iterate over lines
# print(reader)
# print("First Send: %s", time.ctime())
# time.sleep(5)
# print("Second Send: %s", time.ctime())


# # If we no longer want to receive data...
#         answer = str(input("Continue? Yes or No"))
#         if answer == 'no' or 'NO' or 'No' or 'n':
#             break
#         else:
#             # Sleep for 5 seconds to allow for new data be written to the file via FG.
#             time.sleep(5)
