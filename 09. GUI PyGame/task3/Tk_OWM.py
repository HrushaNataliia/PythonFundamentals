import tkinter as tk
from tkinter import font, messagebox
from OWM import get_weather, format_weather_info

HEIGHT = 350
WIDTH = 450

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)


def get_weather_gui():
    city = entry_field.get().strip()

    if not city:
        messagebox.showerror("Помилка", "Введіть назву міста!")
        return

    weather_data = get_weather(city)

    if weather_data:
        weather_text = format_weather_info(weather_data)
        label.config(text=weather_text, justify='left')
    else:
        messagebox.showerror("Помилка", f"Не вдалося знайти погоду для міста: {city}")
        label.config(text="")


button = tk.Button(frame,
                   text="Get Weather",
                   bg="gray", fg="white",
                   font=('Courier', 8),
                   command=get_weather_gui)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 11), bg='gold')
label.place(relx=0, rely=0, relwidth=1, relheight=1)


def on_enter(event):
    get_weather_gui()


entry_field.bind('<Return>', on_enter)

root.mainloop()
