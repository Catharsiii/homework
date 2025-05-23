import tkinter as tk
from tkinter import ttk, StringVar, filedialog, colorchooser, simpledialog

class TextEdit:
    def __init__(self, mainw):
        """Инициализация главного окна и меню"""
        self.mainw = mainw
        self.mainw.geometry("1000x600")
        self.mainw.title("Word x2")
        self.var = StringVar()
        self.current_file = None
        mainw.state('zoomed')

        self.menu_bg = "#f6f6f6"
        self.menu_active_bg = "#e1e1e1"
        self.menu_fg = "#333333"

        self.main_menu = tk.Menu(mainw, bg=self.menu_bg, fg=self.menu_fg, activebackground=self.menu_active_bg, bd=1, relief=tk.FLAT)
        self.file_menu = tk.Menu(self.main_menu, tearoff=0)
        self.edit_menu = tk.Menu(self.main_menu, tearoff=0)
        self.view_menu = tk.Menu(self.main_menu, tearoff=0)
        self.create_widgets()
        self.create_menu()

    def create_widgets(self):
        """Создаёт текстовое поле и скроллбар"""
        scrollbar = ttk.Scrollbar(self.mainw)
        self.text_Window = tk.Text(self.mainw, wrap=tk.WORD, undo=True, yscrollcommand=scrollbar.set,
                                   font=("TimesNewRoman", 12), padx=10, pady=10, selectbackground="#b5d5ff",
                                   inactiveselectbackground="#e6e6e6")

        scrollbar.config(command=self.text_Window.yview)
        self.text_Window.pack(fill="both", expand=True, padx=200)
        scrollbar.pack(side="right", fill="y")

    def new_file(self):
        """Создаёт новый файл (очищает текстовое поле)"""
        self.text_Window.delete("1.0", tk.END)
        self.current_file = None

    def open_file(self):
        """Открывает файл и загружает его содержимое в текстовое поле"""
        file = filedialog.askopenfilename()
        if file:
            with open(file, "r", encoding="utf-8") as f:
                text = f.read()
            self.text_Window.delete("1.0", "end")
            self.text_Window.insert(tk.END, text)
            self.current_file = file

    def save_file_as(self):
        """Сохраняет содержимое текстового поля в новый файл"""
        file = filedialog.asksaveasfilename(defaultextension=".txt")
        if file:
            f = open(file, "w", encoding="utf-8")
            f.write(self.text_Window.get("1.0", tk.END))
            f.close()
            self.current_file = file

    def save_file(self):
        """Сохраняет содержимое текстового поля в текущий файл"""
        if self.current_file:
            with open(self.current_file, "w", encoding="utf-8") as f:
                f.write(self.text_Window.get("1.0", tk.END))
        else:
            self.save_file_as()

    def copy_text(self):
        """Копирует выделенный текст"""
        try:
            self.text_Window.event_generate("<<Copy>>")
        except Exception:
            pass

    def cut_text(self):
        """Вырезает выделенный текст"""
        try:
            self.text_Window.event_generate("<<Cut>>")
        except Exception:
            pass

    def paste_text(self):
        """Вставляет текст из буфера обмена"""
        try:
            self.text_Window.event_generate("<<Paste>>")
        except Exception:
            pass

    def undo_text(self):
        """Отменяет последнее действие"""
        try:
            self.text_Window.edit_undo()
        except Exception:
            pass

    def set_text_color(self):
        """Изменяет цвет текста"""
        color = colorchooser.askcolor()[1]
        if color:
            self.text_Window.config(fg=color)

    def set_font_size(self):
        """Изменяет размер шрифта"""
        size = simpledialog.askinteger("Размер", "Введите размер шрифта:", initialvalue=12)
        if size:
            current_font = self.text_Window.cget("font").split()[0]
            self.text_Window.config(font=(current_font, size))

    def create_menu(self):
        """Создаёт главное меню приложения."""
        self.file_menu.add_command(label="Создать", command=self.new_file)
        self.file_menu.add_command(label="Открыть", command=self.open_file)
        self.file_menu.add_command(label="Сохранить", command=self.save_file)
        self.file_menu.add_command(label="Сохранить как", command=self.save_file_as)

        self.edit_menu.add_command(label="Отменить", command=self.undo_text)
        self.edit_menu.add_command(label="Вырезать", command=self.cut_text)
        self.edit_menu.add_command(label="Копировать", command=self.copy_text)
        self.edit_menu.add_command(label="Вставить", command=self.paste_text)

        self.view_menu.add_command(label="Цвет текста", command=self.set_text_color)
        self.view_menu.add_command(label="Размер шрифта", command=self.set_font_size)

        self.main_menu.add_cascade(label="ФАЙЛ", menu=self.file_menu)
        self.main_menu.add_cascade(label="ПРАВКА", menu=self.edit_menu)
        self.main_menu.add_cascade(label="ВИД", menu=self.view_menu)

        self.mainw.config(menu=self.main_menu)

if __name__ == "__main__":
    root = tk.Tk()
    app = TextEdit(root)
    root.mainloop()