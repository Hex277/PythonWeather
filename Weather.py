import customtkinter
import tkinter as tk
import requests
from PIL import Image

customtkinter.set_appearance_mode("light")

def get_weather():
    city_name = city_entry.get()
    api_key = "YOUR API KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    weather_data = response.json()

    if weather_data["cod"] != "404":
        info_text = (
            f"Weather in {city_name}: {weather_data['weather'][0]['description']}\n"
            f"Temperature: {weather_data['main']['temp']}°C\n"
            f"Feels like: {weather_data['main']['feels_like']}°C\n"
            f"Humidity: {weather_data['main']['humidity']}%\n"
            f"Pressure: {weather_data['main']['pressure']} hPa\n"
            f"Wind Speed: {weather_data['wind']['speed']} m/s\n"
            f"Wind Direction: {weather_data['wind']['deg']}°"
        )
        info_label.configure(text=info_text)
    else:
        info_label.configure(text="City not found!")

root = customtkinter.CTk()
root.title("Weather App")
root.geometry("875x587.5")  # 25% arttırılmış ölçüler

background_image = customtkinter.CTkImage(light_image=Image.open("wbg.jpg"), dark_image=Image.open("wbg.jpg"),
                                          size=(875, 587.5))  # 25% arttırılmış ölçüler
background_label = customtkinter.CTkLabel(root, image=background_image, text="")
background_label.pack()

city_entry = customtkinter.CTkEntry(master=background_label, height=62.5, width=437.5, text_color="#67B5E6", fg_color="white",
                                    font=("helvectica", 43.75), border_color="#67B5E6", bg_color="#67B5E6",
                                    corner_radius=37.5,
                                    justify="center")  # 25% arttırılmış ölçüler
city_entry.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
get_weather_button = customtkinter.CTkButton(master=background_label, height=50, width=312.5, text="Get Weather",
                                             corner_radius=37.5, font=("helvectica", 37.5), text_color="white",
                                             bg_color="#67B5E6", command=lambda: get_weather())
get_weather_button.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

info_label_top = customtkinter.CTkLabel(master=background_label, height=12.5, width=375, fg_color="#67B5E6",
                                        text_color="white",
                                        font=("helvectica", 22.5), bg_color="white",
                                        text="~~~~~~~~ Weather Info ~~~~~~~~")  # 25% arttırılmış ölçüler
info_label_top.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
info_label = customtkinter.CTkLabel(master=background_label, height=300, width=375, fg_color="#67B5E6",
                                    text_color="white",
                                    font=("helvectica", 22.5), bg_color="white",
                                    text="No Weather")  # 25% arttırılmış ölçüler
info_label.place(relx=0.5, rely=0.67, anchor=tk.CENTER)

root.mainloop()
