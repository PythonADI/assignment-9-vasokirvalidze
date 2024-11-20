from tkinter import *
import json


#login form

file_path_registration = "D:\project\output.json"
file_path_information = "D:\project\info.json"

def windowforlogin():

     
    def whensubmit():
        with open(file_path_registration, "r") as file:
            content = json.load(file)
            if content["login"] == login.get() and content["password"] == password.get():

                #page for person
                customer_page = Tk()
                customer_page.geometry("300x300")
                main_window.destroy()

                

                def enter_info():
                    info = {
                    "name": name.get(),
                    "age" : age.get(),
                    "location" : location.get(),
                    "bio" : bio.get()
                }

                    with open(file_path_information, "w") as file:
                        json.dump(info, file)

                name = Entry(customer_page)
                name.insert(0, "Name")
                name.pack()

                age = Entry(customer_page)
                age.insert(0, "Age")
                age.pack()

                location = Entry(customer_page)
                location.insert(0, "location")
                location.pack()

                bio = Entry(customer_page)
                bio.insert(0, "Bio")
                bio.pack()

                submit = Button(customer_page, text="Submit", command=enter_info)
                submit.pack()

               



                customer_page.mainloop()
                    

    login_window = Toplevel()
    login_window.geometry("300x300")

    login_text = Label(login_window, text="login")
    login_text.pack()
    login = Entry(login_window)
    login.pack()

    password_text = Label(login_window, text="password")
    password_text.pack()
    password = Entry(login_window)
    password.pack()

    submit = Button(login_window, text="submit",command=whensubmit)
    submit.pack()


#registration form
def windowforregistration():

    registration_window = Toplevel()
    registration_window.geometry("300x300")

    def whensubmit():
        data = {
        "login" : login.get(),
        "password" : password.get()
            }

        with open(file_path_registration, "w") as file:
            json.dump(data, file)

    login_text = Label(registration_window, text="login")
    login_text.pack()
    login = Entry(registration_window)
    login.pack()

    password_text = Label(registration_window, text="password")
    password_text.pack()
    password = Entry(registration_window)
    password.pack()

    submit = Button(registration_window, text="submit",command=whensubmit)
    submit.pack()



#main window
main_window = Tk()
main_window.geometry("300x300")

signin = Button(main_window, text="sign in",height=1,width=7,command=windowforlogin)
signin.pack()

signup = Button(main_window, text="sign up",height=1,width=7, command=windowforregistration)
signup.pack()


main_window.mainloop()