from tkinter import *
from extract_funcs import techbot_response


def send():
    msg = EntryBox.get("1.0", 'end-1c').strip()
    EntryBox.delete("0.0", END)

    if msg != '':
        chatwin.config(state=NORMAL)
        chatwin.insert(END, "You: " + msg + '\n\n')
        chatwin.config(foreground='green', font=("Arial", 12))

        res = techbot_response(msg)
        chatwin.insert(END, "Bot: " + res + '\n\n')

        chatwin.config(state=DISABLED)
        chatwin.yview(END)


root = Tk()
root.title("tech_bot")
root.geometry("400x500")
root.resizable(width=False, height=False)

chatwin = Text(root, bd=0, bg="black", height="13", width=50, font="Arial", foreground="green")
chatwin.config(state=DISABLED)

scrollbar = Scrollbar(root, command=chatwin.yview(), cursor="heart")
chatwin['yscrollcommand'] = scrollbar.set

sendbutton = Button(root, font=("Arial", 12, 'bold'), text="SEND", width=10, height=1, bd=0, bg='black',
                    activebackground="green", fg="green", command=send)

EntryBox = Text(root, bd=0, bg="black", width=29, height=1, font="Arial", foreground="green", insertbackground="green")

scrollbar.place(x=376, y=6, height=436)
chatwin.place(x=6, y=6, height=436, width=370)
EntryBox.place(x=6, y=450, height=40, width=265)
sendbutton.place(x=280, y=450, height=40)

root.mainloop()
