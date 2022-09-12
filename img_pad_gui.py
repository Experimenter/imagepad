#!/usr/bin/python3
from tkinter import Tk, Frame, Label, Entry, Button, Listbox, filedialog, Spinbox, OptionMenu, Variable, StringVar
from tkinter.messagebox import showinfo
from img_pad import img_pad
from pathlib import Path

root = Tk()

img_files = Variable()
dest_folder = StringVar()
suffix = StringVar(value='.webp')
img_width = StringVar()
img_height = StringVar()


def add_files():
    """Choose image files and add to grid"""
    img_files.set(filedialog.askopenfilenames())


def set_dest():
    dest_folder.set(filedialog.askdirectory())


def convert():
    """Convert chosen files to new image size with padding"""

    # validate target img size #
    if img_width.get().isdigit() and img_height.get().isdigit():
        size = (int(img_width.get()), int(img_height.get()))
    else:
        size = (480, 360)

    for img in img_files.get():
        dest_file = Path(dest_folder.get(), Path(img).with_suffix(suffix.get()).name)
        img_pad(img, dest_file, size)
    showinfo(message="Conversion Complete")


# UI design #
root.title("Image resize and pad")
# root.geometry("360x240")
Button(root, text="Choose image files", command=add_files).pack()
Listbox(root, height=6, width=40, listvariable=img_files).pack()
Button(root, text="Choose destination folder", command=set_dest).pack()
Entry(root, textvariable=dest_folder, width=40, state='readonly').pack(padx=10)
# frame for size input #
sz_frame = Frame(root)
spinvals = (240, 360, 480, 640, 720, 960, 1280)
Spinbox(sz_frame, values=spinvals, width=6, textvariable=img_width).grid(row=1, column=1)
Spinbox(sz_frame, values=spinvals, width=6, textvariable=img_height).grid(row=1, column=3)
Label(sz_frame, text=" x ").grid(row=1, column=2)
Label(sz_frame, text="Format").grid(row=2, column=1, pady=5)
OptionMenu(sz_frame, suffix, '.webp', '.png').grid(row=2, column=3)
sz_frame.pack(pady=5)
# end frame #
Button(root, text="Convert", command=convert).pack(pady=5)

if __name__ == '__main__':
    root.mainloop()
