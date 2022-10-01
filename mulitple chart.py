import tkinter as tk


def multiple():
    number = int(text_input.get())
    window_label1.configure(text=number)

    output = ''
    for i in range(1, 13):
        output += str(number) + ' x ' + str(i)
        output+= ' = ' + str(number*i) + '\n'

    output_label.configure(text=output)


window = tk.Tk()
window.title('multiple')
window.minsize(width= 400 , height= 400)



window_label = tk.Label(master = window,    text = 'multiple chart ' )
window_label.pack(pady= 20)

window_label1 = tk.Label(master = window,    text = '....' )
window_label1.pack()

text_input = tk.Entry(master = window , width= 20)
text_input.pack()

ok_button = tk.Button(master = window,  text= "Okay",   command =multiple , width= 15 , height= 2)
ok_button.pack()

output_label = tk.Label(master = window , text = "waiting.....")
output_label.pack(pady=20)


window.mainloop()



