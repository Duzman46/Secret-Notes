import tkinter
from PIL import Image, ImageTk
import base64

window = tkinter.Tk()
window.config(padx=20, pady=20)
window.title("Secret Notes")
window.geometry("320x680")

def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

def user_input():
    user_input = input1.get()
    user_input2 = input2.get("1.0","end")
    user_input3 = input3.get()
    if len(user_input) == 0 or len(user_input2) == 0 or len(user_input3) == 0:
        import tkinter.messagebox
        tkinter.messagebox.showwarning('Error!', 'Please all enter info!')
    else:
        message_encrypted = encode(user_input3,user_input2)
        with open("user_input.txt", "a") as dosya:
            dosya.write(user_input + "\n"+ message_encrypted + "\n")
        input1.delete(0, "end")
        input2.delete("1.0", "end")
        input3.delete(0, "end")

def decrypt_notes():
    user_input2 = input2.get("1.0","end")
    user_input3 = input3.get()
    if len(user_input2) == 0 or len(user_input3) == 0:
        import tkinter.messagebox
        tkinter.messagebox.showwarning('Error!', 'Please all enter info!')
    else:
        try:
            decrypt_message = decode(user_input3,user_input2)
            input2.delete("1.0","end")
            input2.insert("1.0",decrypt_message)
        except:
            import tkinter.messagebox
            tkinter.messagebox.showwarning('Error!', 'Please enter encrypted text!')
original_image = Image.open("secret_photos.jpg")
new_width = 90
new_height = 75
resized_image = original_image.resize((new_width, new_height))
img = ImageTk.PhotoImage(resized_image)

photo = tkinter.Label(image=img)
photo.pack(pady=35)

message1 = tkinter.Label(text="Enter Your Title",font="Times 11 bold")
message1.pack()

input1 = tkinter.Entry(width=35)
input1.pack()

message2 = tkinter.Label(text="Enter Your Secret",font="Times 11 bold")
message2.pack()

input2 = tkinter.Text(width=35,height=20)
input2.pack()

message3 = tkinter.Label(text="Enter Master Key",font="Times 11 bold")
message3.pack()

input3 = tkinter.Entry(width=35)
input3.pack()

button1 = tkinter.Button(text="Save & Encrypt",command=user_input)
button1.pack()

button2 = tkinter.Button(text="Decrypt",command=decrypt_notes)
button2.pack()

window.mainloop()