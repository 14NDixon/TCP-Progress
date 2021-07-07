import socket
import csv

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostName = "10.0.0.234"
portNumber = 7001

s.connect((socket.gethostname(), portNumber))  # Later connect to a public IP and replace gethostname

msg = s.recv(1000)   # 1024 is the buffer for how big of chunks we expect/can recieve at a time
print(msg.decode("utf-8"))   # decoding to decode from bytes


# SECTION ALPHA - THIS SECTION WORKS, but sometimes has a weird extra line tagged onto a line in long outputs
# THIS SECTION OF CODE RECEIVES THE SENT LINE, DECODES IT TO STR+\n, THEN WIPES THE FILE AND WRITES TO IT AGAIN.
isFirstLine = True

# Open the file 'Transferred Data' and add the last line to the file
with open('Transferred Data', 'w') as f:
    print('Writing the received data to a new file called "Transferred Data"...\n')
    # While we are open to receiving data...
    while True:
        data = s.recv(440)
        string_data = data.decode("utf-8")          # Decode line from bytes to string
        print(string_data)
        data_FirstLine = string_data.rstrip("\n")       # Strip
        data_notFirstLine = string_data.rstrip("\n")

        if isFirstLine:
            f.write(data_FirstLine)
            f.flush()
            isFirstLine = False
        else:
            f.write(data_notFirstLine)

            f.flush()
        if not data:
            break

f.close()

print('Successfully received the data.')
s.close()
print('Connection closed')

# # SECTION BETA - WORKING ON OUTPUTTING TO A CSV FILE
# # THIS SECTION OF CODE RECEIVES THE SENT LINE, DECODES IT TO STR+\n, THEN WIPES THE FILE AND WRITES TO IT AGAIN.
# with open('Transferred Data.csv', 'w', newline='') as csvfile:
#     print('Writing the received data to a new CSV file called "Transferred Data.csv"...\n')
#     while True:
#         data = s.recv(440)
#         # print(data)
#         string_data = data.decode("utf-8")
#         string_data = string_data + '\n'
#         # string_data = string_data
#         print(string_data)
#
#         if not data:
#             break
#         single_row = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#
#         # single_row = csv.writer(csvfile)
#         single_row.writerow(string_data)
# csvfile.close()


