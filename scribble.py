from tkinter import *
from tkinter import filedialog
from tkinter import font

root=Tk()
root.title('Scribble!')
root.geometry("1000x680")

#set variable for open file name
global open_status_name
open_status_name=False
global selected
selected=False


#create newfile function
def new_file():
    my_text.delete("1.0",END)
    root.title('new File-Scribble!')
    status_bar.config(text="New File     ")

    global open_status_name
    open_status_name=False


#opening a file
def open_file():
    #deleting the previous text
    my_text.delete("1.0",END)
    #grab filename
   
    text_file=filedialog.askopenfilename(title="Open file",filetypes=(("Text files","*.txt"),("HTML files","*.html"),("Python files","*.py"),("all files","*.*")))
    #check to see if there is a file name
    if text_file:
        #make filename global so we can access  it later
        global open_status_name
        open_status_name=text_file
    name=text_file
    status_bar.config(text=f'{name}  saved')

#open a file
    text_file=open(text_file,'r')   
    stuff=text_file.read() 
    #add file to text box
    my_text.insert(END,stuff)
    #close the file
    text_file.close()
#save_as
def save_as_file():
    text_file=filedialog.asksaveasfilename(defaultextension=".*",initialdir="C:/",title="save file",filetypes=(("Text files","*.txt"),("HTML files","*.html"),("Python files","*.py"),("all files","*.*")))
    if text_file:
      name=text_file
      status_bar.config(text='saved!')
      #save file
      text_file=open(text_file,'w')
      text_file.write(my_text.get(1.0,END))
      text_file.close()
#save file
def save_file():
    global open_status_name
    if open_status_name:
        text_file=open(open_status_name,'w')
        text_file.write(my_text.get(1.0,END))
        text_file.close()
        

        status_bar.config(text=open_status_name)
    else:
        save_as_file()   
#cut 
def cut_text(e):
    global selected
    if e:
        selected=root.clipboard_get()
    else:    
        if my_text.selection_get():
            #grab selected text from text box
            selected= my_text.selection_get()
            # delete selected txt from txt box
            my_text.delete("sel.first","sel.last")
            root.clipboard_clear()  
            root.clipboard_append(selected)



#copy
def copy_text(e):
    global selected
    # check to see if we used keyboard shortcut
    if e:
        selected=root.clipboard_get()  # this to be done bcuz wtever u have copied in the selection on the top should be remembered by keyboard tht is clipboard
    if my_text.selection_get():
        selected= my_text.selection_get()
        #clear the clipboard thn append
        root.clipboard_clear()  
        root.clipboard_append(selected)

      
#paste
def paste_text(e):
   global selected
   if e:
       selected=root.clipboard_get()
   else:    
        if selected:
            position=my_text.index(INSERT)       # to know the cursor position , grab txt from tht point and insert      
            my_text.insert(position,selected)





      

#create main frame
my_frame=Frame(root)
my_frame.pack(pady=5)

#horizontal scrollbar
hor_scroll=Scrollbar(my_frame,orient='horizontal')
hor_scroll.pack(side=BOTTOM,fill=X)



#scroll bar for the text box
text_scroll=Scrollbar(my_frame)
text_scroll.pack(side=RIGHT,fill=Y)

#create text boxs
my_text=Text(my_frame,width=97,height=25,font=("Helvetica",16),selectbackground="yellow",selectforeground="black",yscrollcommand=text_scroll.set,xscrollcommand=hor_scroll.set,undo=True,wrap="none")
my_text.pack()

#configure our scrollbar
text_scroll.config(command=my_text.yview)
hor_scroll.config(command=my_text.xview)
#menu
my_menu=Menu(root)
root.config(menu=my_menu)

#add file menu
file_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_command(label="SaveAs",command=save_as_file)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)

#add edit menu
edit_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Cut",command=lambda:cut_text(False),accelerator="(Ctrl+x)")
edit_menu.add_command(label="Copy",command=lambda:copy_text(False),accelerator="(Ctrl+c)")
edit_menu.add_command(label="Paste",command=lambda:paste_text(False),accelerator="(Ctrl+v)")
edit_menu.add_separator()
edit_menu.add_command(label="Undo",command=my_text.edit_undo,accelerator="(Ctrl+z)")
edit_menu.add_command(label="Redo",command=my_text.edit_redo,accelerator="(Ctrl+y)")

#adding statusbar to bottom
status_bar=Label(root,text="ready   ",anchor=E)
status_bar.pack(fill=Y,side=TOP)

#edit bindings
root.bind('<Control-Key-x>',cut_text)
root.bind('<Control-Key-c>',copy_text)
root.bind('<Control-Key-v>',paste_text)




root.mainloop()