from tkinter import *
from tkinter import messagebox
from socket import *
from threading import Thread

s = socket(family=AF_INET, type=SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

def recv_thread():
    while True:
        msg = s.recv(500).decode('utf8')
        print(msg)
        # my_msg.set(msg)  # Clears input field....
        msg_list.insert(END, "Server: "+msg)
        msg_list.insert(END, " ")


def send():
    msg = my_msg.get()
    msg_list.insert(END, "Client: "+msg)
    print('data to sent: ', msg)
    my_msg.set("")  # Clears input field.
    s.send(msg.encode('utf-8'))
    msg_list.insert(END, " ")


wind = Tk()
wind.title("CLIENT")
wind.geometry('500x500')

messages_frame = Frame(wind)
my_msg = StringVar()  # For the messages to be sent.
my_msg.set("Type here...")
scrollbar = Scrollbar(messages_frame)  # To navigate through past messages.
# Following will contain the messages.
msg_list = Listbox(messages_frame, height=15, background='#063579',
                   fg='White', width=50, yscrollcommand=scrollbar.set, font=("Calibri", 14))
scrollbar.pack(side=RIGHT, fill=Y)
msg_list.pack(side=LEFT, fill=BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = Entry(wind, textvariable=my_msg, width=30, font=("Calibri", 14))
# entry_field.bind("<Return>", send)
entry_field.pack()
send_button = Button(wind, text="Send", command=send,
                     background='#063579', fg='White', font=("Calibri", 14))
send_button.pack()


host = "127.0.0.1"
port = 7000
addr = (host, port)

print("A, connecting...")
s.connect(addr)
print("A, connected!")

thread_receive = Thread(target=recv_thread)
thread_receive.start()
wind.mainloop()
s.close()
