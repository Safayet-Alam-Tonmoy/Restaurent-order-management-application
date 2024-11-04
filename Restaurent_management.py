import tkinter as tk
from tkinter import messagebox

# Menu items with their prices in a dictionary
foodlist_value = {
    'Pizza': 450, 'Chicken Burger': 120, 'Cheese Burger': 100,
    'Cold Coffee': 80, 'Briyani': 240, 'Chinese': 250,
    'Pasta': 130, 'Chaomin': 150
}
def great(fx):
    def mfx():
        print("Welcome To Our Restaurent")
        fx()
        print("Thank You sir?mam!")
    return mfx

# The main window
window = tk.Tk()
window.title("Restaurant Ordering System")
window.geometry("200x250")

# used to keep track of the order and total cost
order_list = []
total_value = 0

# Function to update the total order cost
def update_total():
    total_label.config(text=f"Total: {total_value} Taka")

# Function to add an item to the order
def add_item(item):
    global total_value
    if item in foodlist_value:
        order_list.append(item)
        total_value += foodlist_value[item]
        order_listbox.insert(tk.END, f"{item} - {foodlist_value[item]} Taka")
        update_total()
    else:
        messagebox.showinfo("Item Not Available", f"Sorry, {item} is not available.")

# Function to finalize the order
def finalize_order():
    if order_list:
        messagebox.showinfo("Order Summary", f"Your total order value is {total_value} Taka. Thank you for ordering!")
        reset_order()
    else:
        messagebox.showinfo("Order Empty", "No items have been added to the order yet.")

# Function to reset the order
def reset_order():
    global total_value, order_list
    total_value = 0
    order_list = []
    order_listbox.delete(0, tk.END)
    update_total()

# Display menu items
menu_label = tk.Label(window, text="Menu",bg='Blue', font=("Arial", 26, "bold"))
menu_label.pack()

for item, price in foodlist_value.items():
    btn = tk.Button(window, text=f"{item} - {price} Taka",bg='pink', command=lambda item=item: add_item(item))
    btn.pack(fill=tk.X, padx=16, pady=1)

# Display the current order list
order_label = tk.Label(window, text="Your Order", bg="yellow",font=("Arial", 16, "bold"))
order_label.pack()

order_listbox = tk.Listbox(window, width=40, height=10)
order_listbox.pack()

# Display the total value of the order
total_label = tk.Label(window, text="Total: 0 Taka", font=("Arial", 14, "bold"))
total_label.pack()

# Add buttons for finalizing and resetting the order
finalize_btn = tk.Button(window, text="Finalize Order", command=finalize_order, bg="green", fg="white", font=("Arial", 16))
finalize_btn.pack(pady=10)

reset_btn = tk.Button(window, text="Reset Order", command=reset_order, bg="red", fg="white", font=("Arial", 12))
reset_btn.pack(pady=5)

# Run the main event loop
window.mainloop()
