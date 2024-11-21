from colorama import Fore
import tkinter as Tk
import requests

bg_color = "#2e2e2e"
fg_color = "#ffffff"
button_bg_color = "#5a5a5a"
button_fg_color = "#ffffff"

icon_path = "ico/ip_icon.ico"

window = Tk.Tk()
window.title("IP Address Finder by EventExecutor")
window.geometry("385x200")
window.configure(bg=bg_color)

window.iconbitmap(icon_path)

def get_ip_address():
    try:
        response = requests.get("https://api.ipify.org?format=json")
        data = response.json()
        ip_address = data['ip']
        label_result.config(text=f"Your IP Address is: {ip_address}", fg="green")
    except Exception as e:
        label_result.config(text="Error to find your IP Address", fg="red")

label_instruction = Tk.Label(window, text="Click the button to get your IP Address:", bg=bg_color, fg=fg_color)
label_instruction.pack(pady=10)

button_get_ip = Tk.Button(window, text="[Get IP]", command=get_ip_address, bg=button_bg_color, fg=button_fg_color)
button_get_ip.pack(pady=10)

label_result = Tk.Label(window, text="", font=("Helvetica", 12), bg=bg_color, fg=fg_color)
label_result.pack(pady=10)

label_info = Tk.Label(window, text="*Not Obfuscated*", font=("Helvetica", 10), bg=bg_color, fg=fg_color)
label_info.pack(pady=10)

window.mainloop()
