import tkinter as tk
from inflect import engine

p = engine()
def b_d(bin_num):
    return int(bin_num, 2)

def d_b(dec_num):
    return bin(dec_num)[2:]

def b_o(bin_num):
    dec_num = b_d(bin_num)
    return oct(dec_num)[2:]

def o_b(oct_num):
    dec_num = int(oct_num, 8)
    return bin(dec_num)[2:]

def b_h(bin_num):
    dec_num = b_d(bin_num)
    return hex(dec_num)[2:]

def h_b(hexd_num):
    dec_num = int(hexd_num, 16)
    return bin(dec_num)[2:]

def d_o(dec_num):
    return oct(dec_num)[2:]

def o_d(oct_num):
    return int(oct_num, 8)

def d_h(dec_num):
    return hex(dec_num)[2:]

def h_d(hexd_num):
    return int(hexd_num, 16)

def o_h(oct_num):
    dec_num = o_d(oct_num)
    return hex(dec_num)[2:]

def h_o(hexd_num):
    dec_num = int(hexd_num, 16)
    return oct(dec_num)[2:]

def convert_to_words(number_str):
    try:
        number = int(number_str)
        words = p.number_to_words(number)
      
        return ', '.join(' '.join(word) for word in words.split())
    except ValueError:
        return "Invalid Input"

def convert_button_click():
    input_val = inpt_entry.get()
    inpt_bas = base_var.get()
    outpt_bas = output_var.get()

    try:
        output_text.delete(1.0, tk.END)  
          
        
        if inpt_bas == 2 and all(c in '01' for c in input_val):
            output_text.insert(tk.END, "....................\n")
            tokens = [int(c) for c in input_val]
            output_text.insert(tk.END, f"Tokens: {tokens}\n")
            word_tokens = [convert_to_words(str(token)) for token in tokens]
            output_text.insert(tk.END, f"Word Tokens: {', '.join(word_tokens)}\n")
        elif inpt_bas == 8 and all(c in '01234567' for c in input_val):
            output_text.insert(tk.END, "....................\n")
            tokens = [int(c) for c in input_val]
            output_text.insert(tk.END, f"Tokens: {tokens}\n")
            word_tokens = [convert_to_words(str(token)) for token in tokens]
            output_text.insert(tk.END, f"Word Tokens: {', '.join(word_tokens)}\n")
        elif inpt_bas == 10 and input_val.isdigit():
            output_text.insert(tk.END, "....................\n")
            tokens = [int(c) for c in input_val]
            output_text.insert(tk.END, f"Tokens: {tokens}\n")
            word_tokens = [convert_to_words(str(token)) for token in tokens]
            output_text.insert(tk.END, f"Word Tokens: {', '.join(word_tokens)}\n")
        elif inpt_bas == 16 and all(c in '0123456789ABCDEFabcdef' for c in input_val):
            output_text.insert(tk.END, "....................\n")
            tokens = [int(c, 16) for c in input_val]
            output_text.insert(tk.END, f"Tokens: {tokens}\n")
            word_tokens = [convert_to_words(str(token)) for token in tokens]
            output_text.insert(tk.END, f"Word Tokens: {', '.join(word_tokens)}\n")
        else:
            raise ValueError("Syntax error (error in input or input base)")
        
       
        if inpt_bas == outpt_bas:
            result = f"The input is already in {outpt_bas}-based format"
        elif inpt_bas == 2 and outpt_bas == 10:
            result = b_d(input_val)
        elif inpt_bas == 10 and outpt_bas == 2:
            result = d_b(int(input_val))
        elif inpt_bas == 2 and outpt_bas == 8:
            result = b_o(input_val)
        elif inpt_bas == 8 and outpt_bas == 2:
            result = o_b(input_val)
        elif inpt_bas == 2 and outpt_bas == 16:
            result = b_h(input_val)
        elif inpt_bas == 16 and outpt_bas == 2:
            result = h_b(input_val)
        elif inpt_bas == 10 and outpt_bas == 8:
            result = d_o(int(input_val))
        elif inpt_bas == 8 and outpt_bas == 10:
            result = o_d(input_val)
        elif inpt_bas == 10 and outpt_bas == 16:
            result = d_h(int(input_val))
        elif inpt_bas == 16 and outpt_bas == 10:
            result = h_d(input_val)
        elif inpt_bas == 8 and outpt_bas == 16:
            result = o_h(input_val)
        elif inpt_bas == 16 and outpt_bas == 8:
            result = h_o(input_val)
        else:
            raise ValueError("Invalid Conversion")

        cnvrsion_result.set(f"Result: {result}")
        
        output_text.insert(tk.END, "DONE...............\n")

        error_msg.set("")
    except ValueError as e:
        error_msg.set(str(e))
        output_text.insert(tk.END, f"Error: {e}\n", "red")

def reset_button_click():
    inpt_entry.delete(0, tk.END)
    cnvrsion_result.set("")
    error_msg.set("")
    output_text.delete(1.0, tk.END)

window = tk.Tk()
window.title("OS Project by 005, 042, 045")

titl_lble = tk.Label(window, text="NUMBER CONVERSION SYSTEM", font=("helvetica", 16), fg="blue")
titl_lble.pack(pady=10)
inpt_frme = tk.Frame(window)
inpt_frme.pack(pady=10)

tk.Label(inpt_frme, text="Input Number:", font=("Arial", 12), fg="blue").grid(row=0, column=0, padx=5)
inpt_entry = tk.Entry(inpt_frme, font=("Arial", 12))
inpt_entry.grid(row=0, column=1, padx=5)

int_frme = tk.Frame(window)
int_frme.pack(pady=10)

outpt_frme = tk.Frame(window)
outpt_frme.pack(pady=10)

tk.Label(int_frme, text="Input Base:", font=("Arial", 12), fg="blue").grid(row=0, column=0, pady=5)
base_var = tk.IntVar()
inpt_bas_radio_bin = tk.Radiobutton(int_frme, text="Binary", variable=base_var, value=2, font=("Arial", 12), fg="Navy blue")
inpt_bas_radio_bin.grid(row=0, column=1)
inpt_bas_radio_oct = tk.Radiobutton(int_frme, text="Octal", variable=base_var, value=8, font=("Arial", 12), fg="Navy blue")
inpt_bas_radio_oct.grid(row=0, column=2)
input_base_radio_dec = tk.Radiobutton(int_frme, text="Decimal", variable=base_var, value=10, font=("Arial", 12), fg="Navy blue")
input_base_radio_dec.grid(row=0, column=3)
input_base_radio_hex = tk.Radiobutton(int_frme, text="Hexadecimal", variable=base_var, value=16, font=("Arial", 12), fg="Navy blue")
input_base_radio_hex.grid(row=0, column=4)

tk.Label(outpt_frme, text="Output Base:", font=("Arial", 12), fg="blue").grid(row=1, column=0, pady=5)
output_var = tk.IntVar()
outpt_bas_radio_bin = tk.Radiobutton(outpt_frme, text="Binary", variable=output_var, value=2, font=("Arial", 12), fg="Navy blue")
outpt_bas_radio_bin.grid(row=1, column=1)
outpt_bas_radio_oct = tk.Radiobutton(outpt_frme, text="Octal", variable=output_var, value=8, font=("Arial", 12),  fg="Navy blue")
outpt_bas_radio_oct.grid(row=1, column=2)
output_base_radio_dec = tk.Radiobutton(outpt_frme, text="Decimal", variable=output_var, value=10, font=("Arial", 12), fg="Navy blue")
output_base_radio_dec.grid(row=1, column=3)
output_base_radio_hex = tk.Radiobutton(outpt_frme, text="Hexadecimal", variable=output_var, value=16, font=("Arial", 12), fg="Navy blue")
output_base_radio_hex.grid(row=1, column=4)

convert_button = tk.Button(window, text="Convert", command=convert_button_click, bg="green", font=("Arial", 12))
convert_button.pack(pady=10)

reset_button = tk.Button(window, text="Reset", command=reset_button_click, bg="yellow", font=("Arial", 12))
reset_button.pack(pady=10)

cnvrsion_result = tk.StringVar()
result_label = tk.Label(window, textvar=cnvrsion_result, font=("Arial", 12))
result_label.pack(pady=10)

error_msg = tk.StringVar()
error_label = tk.Label(window, textvar=error_msg, font=("Arial", 12), fg="red")
error_label.pack(pady=10)

output_text = tk.Text(window, height=10, width=60, wrap=tk.WORD, fg="black")
output_text.pack(pady=10)

window.mainloop()
