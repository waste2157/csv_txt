import csv
import sys
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def process_csv():
    csv_file = filedialog.askopenfilename(title="Select CSV File", filetypes=[("CSV Files", "*.csv")])
    if csv_file:
        try:
            unique_entries = set()  # Set to store unique combinations of IP addresses and ports

            with open(csv_file, 'r') as csvfile:
                reader = csv.reader(csvfile)
                file_name = os.path.splitext(os.path.basename(csv_file))[0]
                output_file = f'{file_name}_output.txt'

                with open(output_file, 'w') as txtfile:
                    next(reader)  # Skip the first row (headers)
                    for row in reader:
                        host = row[0]  # IP address column
                        port = row[1]  # Port column

                        if port != '0':
                            entry = f'{host}:{port}'
                            if entry not in unique_entries:
                                unique_entries.add(entry)
                                txtfile.write(f'{host}:{port}\n')
                                print(f'{host}:{port}')

            messagebox.showinfo("CSV Processing", "CSV file processed successfully.")
        except Exception as e:
            messagebox.showerror("CSV Processing Error", str(e))
    else:
        messagebox.showwarning("CSV Processing", "No CSV file selected.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("CSV to Text Converter")

    button = tk.Button(root, text="Select CSV File", command=process_csv)
    button.pack(padx=120, pady=60)

    root.mainloop()
