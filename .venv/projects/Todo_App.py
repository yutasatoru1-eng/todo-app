import functions
import FreeSimpleGUI as fsg

label= fsg.Text("Type in a To do")
input= fsg.InputText(tooltip="Enter Todo",key="todo")
add_buton=fsg.Button("Add")

window=fsg.Window('My To-Do App',layout=[[label],[input,add_buton]],font=('Helvetica',20))

while True:
    event,values=window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos= functions.get_todos()
            new_todo=values["todo"]+ "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case fsg.WIN_CLOSED:
            break

window.close()