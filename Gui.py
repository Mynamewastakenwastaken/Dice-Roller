from tkinter import *

root = Tk()
root.title("Dice Roller")


class Dice(object):
    dice_pool = []

    def __init__(self, faces, primary=0, crit_behavior=0, crit_value=1, state=0, amount=1, weight=0):
        self.faces = faces
        self.primary = primary
        self.crit_behavior = crit_behavior
        self.crit_value = crit_value
        self.state = state
        self.amount = amount
        self.weight = weight
        Dice.dice_pool.append(self)


Die_frame = LabelFrame(root, text="Dice", padx=8, pady=8)
Die_frame.pack(padx=10, pady=10, side=LEFT, fill=BOTH)
Skill_frame = LabelFrame(root, text="Skills", padx=8, pady=8)
Skill_frame.pack(padx=10, pady=10, side=TOP)
Options_frame = LabelFrame(root, text="Options", padx=8, pady=8)
Options_frame.pack(padx=10, pady=10, side=BOTTOM, fill=BOTH)

Select_Label = Label(Die_frame, text="Define dice").grid(row=0, column=2)
Amount_Label = Label(Die_frame, text="Amt").grid(row=0, column=3)
Crit_Label = Label(Die_frame, text="Crit value -").grid(row=11, column=2)
Crit_Label = Label(Die_frame, text="Behavior").grid(row=11, column=2, padx=(20, 0), columnspan=3)
check_values = []
all_value = IntVar()
Check_all = Checkbutton(Die_frame, variable=all_value, command=lambda: all_check()).grid(row=0, column=1)


def all_check():
    if all_value.get():
        for i in range(0, check_length):
            check_values[i].set(1)
    else:
        for i in range(0, check_length):
            check_values[i].set(0)
    enable_check_face()


def enable_check_face():
    for i in range(0, 10):
        if check_values[i].get() == 0:
            Entrybox_Widget.Face_objects[i].configure(state=DISABLED)
            Entrybox_Widget.Amount_objects[i].configure(state=DISABLED)
        else:
            Entrybox_Widget.Face_objects[i].configure(state=NORMAL)
            Entrybox_Widget.Amount_objects[i].configure(state=NORMAL)
            if Entrybox_Widget.Amount_values[i].get() == 0:
                Entrybox_Widget.Amount_objects[i].delete(0, END)
                Entrybox_Widget.Amount_objects[i].insert(0, 1)


def enable_check_skill():
    for i in range(0, 10):
        if skill_values[i].get() == 0:
            Entrybox_Widget.Cost_objects[i].configure(state=DISABLED)
            Entrybox_Widget.Damage_objects[i].configure(state=DISABLED)
            repeat_objects[i].configure(state=DISABLED)
            initiate_objects[i].configure(state=DISABLED)
            depend_objects[i].configure(state=DISABLED)
        else:
            Entrybox_Widget.Cost_objects[i].configure(state=NORMAL)
            Entrybox_Widget.Damage_objects[i].configure(state=NORMAL)
            repeat_objects[i].configure(state=NORMAL)
            initiate_objects[i].configure(state=NORMAL)
            depend_objects[i].configure(state=NORMAL)


def initiator_switch():
    for i in range(0, 10):
        if initiate_values[i].get() == 1:
            depend_values[i].set(0)


def dependant_switch():
    for i in range(0, 10):
        if depend_values[i].get() == 1:
            initiate_values[i].set(0)


for i in range(0, 10):  # creating checkboxes
    value_inside = IntVar()
    value_inside.set(0)
    check = Checkbutton(Die_frame, variable=value_inside, command=lambda: enable_check_face())
    check.grid(row=i + 1, column=1)
    check_values.append(value_inside)
check_length = len(check_values)

Skill_value = IntVar()
Skill_check = Checkbutton(Skill_frame, variable=Skill_value, command=lambda: all_skillcheck()).grid(row=0, column=0)


def all_skillcheck():  # all-checkbox function
    if Skill_value.get():
        for i in range(0, check_length):
            skill_values[i].set(1)
    else:
        for i in range(0, check_length):
            skill_values[i].set(0)
    enable_check_skill()


skill_values = []
repeat_values = []
repeat_objects = []
initiate_values = []
initiate_objects = []
depend_values = []
depend_objects = []

# Skills: Cost, Damage, Repeatable, initiator/dependant, Skill point carryover between rolls
for i in range(0, 10):  # creating skill checkboxes
    value_inside = IntVar()
    value_inside.set(0)
    check = Checkbutton(Skill_frame, variable=value_inside, command=lambda: enable_check_skill())
    check.grid(row=i + 1, column=0)
    skill_values.append(value_inside)

for i in range(0, 10):  # creating repeatable checkboxes
    value_inside = IntVar()
    value_inside.set(0)
    check = Checkbutton(Skill_frame, variable=value_inside, state=DISABLED)
    check.grid(row=i + 1, column=3, padx=(8, 0))
    repeat_objects.append(check)
    repeat_values.append(value_inside)

for i in range(0, 10):  # creating initiate checkboxes
    value_inside = IntVar()
    value_inside.set(0)
    check = Checkbutton(Skill_frame, variable=value_inside, command=lambda: initiator_switch(), state=DISABLED)
    check.grid(row=i + 1, column=4, padx=(8, 0))
    initiate_objects.append(check)
    initiate_values.append(value_inside)

for i in range(0, 10):  # creating dependant checkboxes
    value_inside = IntVar()
    value_inside.set(0)
    check = Checkbutton(Skill_frame, variable=value_inside, command=lambda: dependant_switch(), state=DISABLED)
    check.grid(row=i + 1, column=5, padx=(8, 0))
    depend_objects.append(check)
    depend_values.append(value_inside)


carry_check_label = Label(Skill_frame, text="point carry-over").grid(row=11, column=1, pady=(8, 0), columnspan=2)
carry_check_value = []
carry_check_inside = IntVar()
carry_check = Checkbutton(Skill_frame, variable=carry_check_inside)
carry_check.grid(row=11, column=3, padx=(8, 0), pady=(10, 0))
carry_check_value.append(carry_check_inside)

def char_length(i):  # limit only numbers and set max character limit
    if len(i) == 0:
        return True
    elif len(i) < 4 and i.isdigit():
        return True
    else:
        return False


def char_numeric(i):  # limit only numbers
    if len(i) < 8 and i.isdigit() and int(i) >= 1:
        return True
    else:
        return False


#entrybox validations
clcmd = (root.register(char_length), '%P')
cncmd = (root.register(char_numeric), '%P')

#labels
Cost_Label = Label(Skill_frame, text="cost   -").grid(row=0, column=1, padx=(8, 0))
Damage_Label = Label(Skill_frame, text="value").grid(row=0, column=2)
Repeat_Label = Label(Skill_frame, text="∞").grid(row=0, column=3, padx=(5, 0))
Initiator_Label = Label(Skill_frame, text="1").grid(row=0, column=4)
Dependant_Label = Label(Skill_frame, text="0").grid(row=0, column=5)
Repeat_Label = Label(Options_frame, text="Rolls:").grid(row=2, column=0, padx=(0, 40))
Graph_Label = Label(Options_frame, text="Graph range:").grid(row=4, column=0)
Cost_values = []


class Entrybox_Widget():
    Face_objects = []
    Amount_objects = []
    Cost_objects = []
    Damage_objects = []
    Face_values = []
    Amount_values = []
    Crit_value = []
    Cost_values = []
    Damage_values = []
    Repeat_value = []
    Graph_value = []

    def add_face_entry(self):  # defining all entryboxes
        value_inside = StringVar()
        entry = Entry(Die_frame, width=40, textvariable=value_inside, state=DISABLED)
        entry.grid(row=i + 1, column=2, padx=(2, 4))
        entry.insert(0, '')
        Entrybox_Widget.Face_objects.append(entry)
        Entrybox_Widget.Face_values.append(value_inside)

    def add_amount_entry(self):
        value_inside = IntVar()
        entry = Entry(Die_frame, width=4, validate="key", validatecommand=clcmd, textvariable=value_inside,
                      state=DISABLED)
        entry.grid(row=i + 1, column=3, padx=(2, 4))
        Entrybox_Widget.Amount_objects.append(entry)
        Entrybox_Widget.Amount_values.append(value_inside)

    def add_cost_entry(self):
        value_inside = IntVar()
        entry = Entry(Skill_frame, width=4, validate="key", validatecommand=clcmd, textvariable=value_inside,
                      state=DISABLED)
        entry.grid(row=i + 1, column=1)
        Entrybox_Widget.Cost_objects.append(entry)
        Entrybox_Widget.Cost_values.append(value_inside)

    def add_damage_entry(self):
        value_inside = IntVar()
        entry = Entry(Skill_frame, width=4, validate="key", validatecommand=clcmd, textvariable=value_inside,
                      state=DISABLED)
        entry.grid(row=i + 1, column=2, padx=5)
        Entrybox_Widget.Damage_objects.append(entry)
        Entrybox_Widget.Damage_values.append(value_inside)

    def add_crit_entry(self):
        value_inside = IntVar()
        value_inside.set(1)
        entry = Entry(Die_frame, width=4, validate="key", validatecommand=clcmd, textvariable=value_inside)
        entry.grid(row=12, column=2)
        Entrybox_Widget.Crit_value.append(value_inside)

    def add_rolls_entry(self):
        value_inside = IntVar()
        value_inside.set(100000)
        entry = Entry(Options_frame, width=8, validate="key", validatecommand=cncmd, textvariable=value_inside)
        entry.grid(row=2, column=1, pady=5, padx=(38, 0))
        Entrybox_Widget.Repeat_value.append(value_inside)

    def add_graph_entry(self):
        value_inside = IntVar()
        value_inside.set(i*9+1)
        entry = Entry(Options_frame, width=4, validate="key", validatecommand=clcmd, textvariable=value_inside)
        entry.grid(row=4, column=i+1, columnspan=2)
        Entrybox_Widget.Graph_value.append(value_inside)


for i in range(0, 10):  # creating entryboxes
    Entrybox_Widget.add_face_entry(i)
    Entrybox_Widget.add_amount_entry(i)
    Entrybox_Widget.add_cost_entry(i)
    Entrybox_Widget.add_damage_entry(i)
    if i < 2:
        Entrybox_Widget.add_graph_entry(i)
    if i < 1:
        Entrybox_Widget.add_crit_entry(i)
        Entrybox_Widget.add_rolls_entry(i)

crit_options = '∞', '2x'
crit_value_type = IntVar()
crit_value = []

critmenu = OptionMenu(Die_frame, crit_value_type, *crit_options)
crit_value_type.set(crit_options[0])
critmenu.grid(row=12, column=2, padx=(20, 0), columnspan=3)
crit_value.append(crit_value_type)

drop_options = 'Sum', 'Max', 'Min'
drop_values = []

for i in range(0, 10):  # creating drop menu's
    value_inside = StringVar()
    value_inside.set(drop_options[0])
    dropmenu = OptionMenu(Die_frame, value_inside, *drop_options)
    dropmenu.grid(row=i + 1, column=4)
    drop_values.append(value_inside)

test_button = Button(Options_frame, text='test', command=lambda: execute()).grid(row=5, column=5)


def show():  # test function
    temp = []
    for i in range(0, 10):
        if check_values[i].get():
            temp.append(drop_values[i].get())
        else:
            temp.append('x')
    print(temp)
    print('-----------')


def show2():
    temp = []
    for i in range(0, 10):
        temp.append(Entrybox_Widget.Face_objects[i])
    print(temp)
    # for i in range(0, 10):
    # temp.append(Entrybox_Widget.Cost_values[i].get())
    # print(temp)


def show3():
    temp = []
    for i in range(0, 10):
        if check_values[i].get():
            temp.append(Entrybox_Widget.Face_values[i].get())
        else:
            temp.append('x')
    print(temp)
    print('-----------')


def execute():
    temp = []
    for i in range(0, 2):
        temp.append(Entrybox_Widget.Graph_value[i].get())
    print(temp)


def Dice_Correct(*args):  # function to return readable dice
    for x in args:
        if ',' in x:
            return x
        else:
            temp = list([val for val in x if val.isnumeric()])
            return "".join(temp)


def Dice_Construct(*args):
    for x in args:
        if ',' in x:
            temp = [float(e) for e in x.split(',')]
            return temp
        else:
            size = int(x)
            temp = []
            for i in range(0, size):
                temp.append(i + 1)
            return temp


root.mainloop()
