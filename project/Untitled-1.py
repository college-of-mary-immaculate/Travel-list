import tkinter as tk
import json

def setup_ui():
    global main_frame, search_frame, about_frame, car_frame, done_frame, todo_vars

    todo_vars = []

    container = tk.Frame(root, bg='royal blue')
    container.pack(expand=False, fill="both")

    main_frame = tk.Frame(container, bg='light blue')
    about_frame = tk.Frame(container, bg='light blue')
    search_frame = tk.Frame(container, bg='royal blue')
    car_frame = tk.Frame(container, bg='royal blue')
    done_frame = tk.Frame(container, bg='royal blue')

    for frame in (main_frame, search_frame, about_frame, car_frame, done_frame):
        frame.grid(row=0, column=0, sticky="nsew")

    create_mainframe()
    create_aboutframe()
    create_searchframe()
    create_carframe()
    create_doneframe()
    
    completed_tasks()
    show_frame(main_frame)
def completed_tasks():
    try:
        with open('completed_tasks.json', 'r') as f:
            completed_tasks = json.load(f)
            for task in completed_tasks:
                done_listbox.insert(tk.END, task)
    except FileNotFoundError:
        pass
def create_mainframe():
    global bg_label
    label = tk.Label(main_frame, text="Welcome to Travel Bud", font=custom_font, bg='light blue', fg='white')
    label.pack(pady=100)
    
    bg_image = tk.PhotoImage(file='Fun and Creative.png')
    bg_image = bg_image.subsample(4, 4) 
    bg_label = tk.Label(main_frame, image=bg_image)
    
    bg_label.image = bg_image
    bg_label.place(relwidth=1, relheight=1)

    search_button = tk.Button(main_frame, text="OPEN", command=lambda: show_frame(search_frame))
    search_button.pack()

    about_button = tk.Button(main_frame, text="ABOUT US", command=lambda: show_frame(about_frame))
    about_button.pack()
    exit_button = tk.Button(main_frame, text="EXIT", command=root.destroy)
    exit_button.pack()

def create_aboutframe():
    global bg_label_about
    bg_image_about = tk.PhotoImage(file='Fun and Creative2.png')
    bg_image_about = bg_image_about.subsample(4, 5)
    bg_label_about = tk.Label(about_frame, image=bg_image_about)
    bg_label_about.image = bg_image_about
    bg_label_about.place(relwidth=1, relheight=1)

    
    button1 = tk.Button(about_frame, text="BACK", command=lambda: show_frame(main_frame))
    button1.place(x=10, y=10)

def create_searchframe():
    global entry, output
    label2 = tk.Label(search_frame, text="TRAVEL BUD!", bg='royal blue', fg='ORANGE', font=custom_font)
    label2.pack(padx=10, pady=5, side=tk.TOP, fill=tk.BOTH)

    def click(event):
        entry.config(state="normal")
        entry.delete(0, "end")

    entry = tk.Entry(search_frame, width=20, bg='white', fg="black")
    entry.pack(padx=40, pady=40, fill=tk.X)
    entry.insert(0, "SEARCH")
    entry.config(state="disabled")
    entry.bind("<Button-1>", click)
    entry.bind("<KeyRelease>", searching)

    output = tk.Text(search_frame, height=15, width=12, bg='light blue', fg="black")
    output.config(state=tk.DISABLED)
    output.pack(padx=1, pady=1, fill=tk.BOTH)

    buttons_frame = tk.Frame(search_frame, bg="royal blue")
    buttons_frame.pack(side=tk.BOTTOM, padx=10, pady=10, fill=tk.BOTH)

    button1 = tk.Button(buttons_frame, width=7, text="SEARCH", cursor='hand2', command=lambda: show_frame(search_frame))
    button1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    button2 = tk.Button(buttons_frame, width=7, text="CAR", cursor='hand2', command=lambda: show_frame(car_frame))
    button2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    button3 = tk.Button(buttons_frame, width=7, text="DONE", cursor='hand2', command=lambda: show_frame(done_frame))
    button3.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

    buttons_frame.grid_columnconfigure(0, weight=1)
    buttons_frame.grid_columnconfigure(1, weight=1)
    buttons_frame.grid_columnconfigure(2, weight=1)

    back_button = tk.Button(search_frame, text="BACK", command=lambda: show_frame(main_frame))
    back_button.place(x=10, y=10)

def create_carframe():
    global todo_entry, todo_list_frame, canvas

    label3 = tk.Label(car_frame, text='CAR TASK LIST', bg="royal blue", fg='ORANGE', font=custom_font)
    label3.pack(padx=5, pady=10, fill=tk.BOTH)

    entry_frame = tk.Frame(car_frame, bg="royal blue")
    entry_frame.pack()

    todo_entry = tk.Entry(entry_frame, width=25)
    todo_entry.pack(side=tk.LEFT, padx=(0, 2), pady=10)

    add_button = tk.Button(entry_frame, text="Add Task", cursor='hand2', command=add_todo_item)
    add_button.pack(side=tk.LEFT, pady=10)

    todo_frame = tk.Frame(car_frame, bg='light blue')
    todo_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    canvas = tk.Canvas(todo_frame, bg='light blue', bd=0, highlightthickness=0)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    todo_list_frame = tk.Frame(canvas, bg='light blue')
    canvas.create_window((0, 0), window=todo_list_frame, anchor='nw')

    canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))
    todo_list_frame.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))

    buttons_frame = tk.Frame(car_frame, bg="royal blue")
    buttons_frame.pack(padx=10, pady=10, fill=tk.BOTH)

    button1 = tk.Button(buttons_frame, width=7, text="SEARCH", cursor='hand2', command=lambda: show_frame(search_frame))
    button1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    button2 = tk.Button(buttons_frame, width=7, text="CAR", cursor='hand2', command=lambda: show_frame(car_frame))
    button2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    button3 = tk.Button(buttons_frame, width=7, text="DONE", cursor='hand2', command=lambda: show_frame(done_frame))
    button3.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
    
    buttons_frame.grid_columnconfigure(0, weight=1)
    buttons_frame.grid_columnconfigure(1, weight=1)
    buttons_frame.grid_columnconfigure(2, weight=1)

    back_button = tk.Button(car_frame, text="BACK", command=lambda: show_frame(main_frame))
    back_button.place(x=10, y=10)

def create_doneframe():
    global done_listbox

    label3 = tk.Label(done_frame, text='COMPLETED TASKS', bg="royal blue", fg='ORANGE', font=custom_font)
    label3.pack(padx=10, pady=10, fill=tk.BOTH)

    done_listbox = tk.Listbox(done_frame, width=30, height=20, bg='light blue', fg="black")
    done_listbox.pack(padx=10, pady=10, fill=tk.BOTH)

    buttons_frame = tk.Frame(done_frame, bg="royal blue")
    buttons_frame.pack(side=tk.BOTTOM, padx=10, pady=10, fill=tk.BOTH)

    button1 = tk.Button(buttons_frame, width=7, text="SEARCH", cursor='hand2', command=lambda: show_frame(search_frame))
    button1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    button2 = tk.Button(buttons_frame, width=7, text="CAR", cursor='hand2', command=lambda: show_frame(car_frame))
    button2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    button3 = tk.Button(buttons_frame, width=7, text="DONE", cursor='hand2', command=lambda: show_frame(done_frame))
    button3.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

    buttons_frame.grid_columnconfigure(0, weight=1)
    buttons_frame.grid_columnconfigure(1, weight=1)
    buttons_frame.grid_columnconfigure(2, weight=1)

    back_button = tk.Button(done_frame, text="BACK", command=lambda: show_frame(main_frame))
    back_button.place(x=10, y=10)

def show_frame(frame):
    frame.tkraise()

def add_todo_item():
    global todo_vars

    item_text = todo_entry.get().strip()
    if item_text:
        var = tk.BooleanVar()
        checkbox = tk.Checkbutton(todo_list_frame, text=item_text, variable=var, bg='royal blue')
        checkbox.pack(anchor='w', padx=10, pady=2)
        var.trace_add('write', lambda *args, var=var, text=item_text: done(var, text))
        todo_vars.append((item_text, var))
        todo_entry.delete(0, tk.END)
        sort_todo_list()

def done(var, text):
    global todo_vars

    if var.get():
        done_listbox.insert(tk.END, text)
        todo_vars = [(t, v) for t, v in todo_vars if t != text]
        sort_todo_list()
        save()

def quicksort(items):
    if len(items) <= 1:
        return items
    pivot = items[len(items) // 2]
    left = [x for x in items if x < pivot]
    middle = [x for x in items if x == pivot]
    right = [x for x in items if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def sort_todo_list():
    sorted_items = quicksort([item[0] for item in todo_vars])
    for widget in todo_list_frame.winfo_children():
        widget.destroy()

    for item_text in sorted_items:
        for text, var in todo_vars:
            if text == item_text:
                checkbox = tk.Checkbutton(todo_list_frame, text=text, variable=var, bg='light blue')
                checkbox.pack(anchor='w', padx=10, pady=2)

def searching(event):
    global output

    input_str = entry.get().strip().lower()
    output.config(state=tk.NORMAL)
    output.delete(1.0, tk.END)

    if input_str == "":
        output.config(state=tk.DISABLED)
        return

    words = []
    min_distance = float('inf')

    for dict_word in dictionary:
        distance = comparing(input_str, dict_word)
        if distance < min_distance:
            words = [dict_word]
            min_distance = distance
        elif distance == min_distance:
            words.append(dict_word)

    for word in words:
        button = tk.Button(output, text=f'Add to car: {word}', cursor='plus', command=lambda w=word: add_tasklist(w))
        output.window_create("end", window=button)
        output.insert("end", "\n")

    output.config(state=tk.DISABLED)

def comparing(str1, str2):
    m = len(str1)
    n = len(str2)

    arr = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                arr[i][j] = j
            elif j == 0:
                arr[i][j] = i
            elif str1[i - 1] == str2[j - 1]:
                arr[i][j] = arr[i - 1][j - 1]
            else:
                arr[i][j] = 1 + min(arr[i][j - 1], arr[i - 1][j], arr[i - 1][j - 1])

    return arr[m][n]

def add_tasklist(word):
    todo_entry.insert(tk.END, word)
    add_todo_item()

def save():
    completed_tasks = [done_listbox.get(idx) for idx in range(done_listbox.size())]
    with open('completed_tasks.json', 'w') as f:
        json.dump(completed_tasks, f, indent=4)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Travel Bud")
    root.geometry("400x470")
    root.resizable(False, False)
    root.iconbitmap('landscape_Bva_icon.ico')

    custom_font = ("Helvetica", 14, "bold italic")

    dictionary =  [
            "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda",
            "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas",
            "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize",
            "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil",
            "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia",
            "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China",
            "Colombia", "Comoros", "Congo, Democratic Republic of the", "Congo, Republic of the",
            "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark",
            "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador",
            "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji",
            "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana",
            "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana",
            "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran",
            "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan",
            "Kazakhstan", "Kenya", "Kiribati", "Korea, North", "Korea, South", "Kosovo",
            "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia",
            "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi",
            "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania",
            "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia",
            "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru",
            "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria",
            "North Macedonia", "Norway", "Oman", "Pakistan", "Palau", "Palestine",
            "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland",
            "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis",
            "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino",
            "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles",
            "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands",
            "Somalia", "South Africa", "South Sudan", "Spain", "Sri Lanka", "Sudan",
            "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan",
            "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago",
            "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine",
            "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan",
            "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"
        ]
    setup_ui()
    root.mainloop()