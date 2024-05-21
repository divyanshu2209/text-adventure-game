import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Jungle Adventure")
window.geometry("400x500")

game_state = {
    "location": "start",
    "inventory": []
}

def update_game_text(text):
    game_text.delete("1.0", tk.END)
    game_text.insert(tk.END, text)

def process_input():
    user_input = input_variable.get().lower()

    if game_state["location"] == "start":
        if user_input == "look":
            update_game_text("You find yourself trapped in a dense jungle. What do you do?")
        elif user_input == "search":
            game_state["inventory"].extend(["machete", "rope"])
            game_state["location"] = "jungle"
            update_game_text("You search for tools and find a machete and a coil of rope.\n"
                             "Armed with the machete and rope, you venture deeper into the jungle.")
        else:
            update_game_text("Invalid command. Try again.")

    elif game_state["location"] == "jungle":
        if user_input == "look":
            update_game_text("You encounter a ferocious tiger blocking your path. What do you do?")
        elif user_input == "fight" and "machete" in game_state["inventory"]:
            update_game_text("With a swift swing of your machete, you defeat the tiger and proceed forward.")
            game_state["location"] = "river"
        elif user_input == "fight" and "machete" not in game_state["inventory"]:
            update_game_text("You attempt to fight the tiger bare-handed but get severely injured. Game over!")
            game_over()
        else:
            update_game_text("Invalid command. Try again.")

    elif game_state["location"] == "river":
        if user_input == "look":
            update_game_text("You reach a wide river. How do you proceed?")
        elif user_input == "swim":
            update_game_text("You attempt to swim across the river but get caught in the strong current. Game over!")
            game_over()
        elif user_input == "build" and "rope" in game_state["inventory"]:
            update_game_text("You use the rope and your survival skills to construct a sturdy makeshift bridge.")
            game_state["location"] = "treasure"
        elif user_input == "build" and "rope" not in game_state["inventory"]:
            update_game_text("You don't have anything to build a bridge with. Find something suitable.")
        else:
            update_game_text("Invalid command. Try again.")

    elif game_state["location"] == "treasure":
        if user_input == "look":
            update_game_text("Congratulations! You've reached the end of the jungle and discovered a hidden treasure.")
            game_over()
        else:
            update_game_text("Invalid command. Try again.")

def game_over():
    messagebox.showinfo("Game Over", "Thank you for playing!")
    window.destroy()

def start_new_game():
    game_state["location"] = "start"
    game_state["inventory"] = []
    update_game_text("You find yourself trapped in a dense jungle. What do you do?")

# Create menu
menu_bar = tk.Menu(window)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New Game", command=start_new_game)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)
menu_bar.add_cascade(label="File", menu=file_menu)
window.config(menu=menu_bar)

game_text = tk.Text(window, height=20, width=40)
game_text.pack()

input_variable = tk.StringVar(window)
input_entry = tk.Entry(window, textvariable=input_variable, width=40)
input_entry.pack()

submit_button = tk.Button(window, text="Submit", command=process_input)
submit_button.pack()

# Add hints near the submit button
hints_label = tk.Label(window, text="Hints:")
hints_label.pack()

hints_text = tk.Text(window, height=6, width=40)  # Increased height to 6
hints_text.insert(tk.END, "Available Commands:\n- look\n- search\n- fight\n- run\n- swim\n- build")
hints_text.configure(state="disabled")
hints_text.pack()

update_game_text("You find yourself trapped in a dense jungle. What do you do?")

window.mainloop()
