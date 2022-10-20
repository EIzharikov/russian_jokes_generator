from tkinter import *

from message_request import MessageRequest
from src.constants import BG_GRAY, BG_COLOR, TEXT_COLOR, FONT, FONT_BOLD, MESSAGE_ENTRY_BOX_COLOR


class Application:
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()
        self.mes_request = MessageRequest()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("JOKE GENERATOR")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=620, bg=BG_COLOR)

        # head label
        head_label = Label(
            self.window,
            bg=BG_COLOR,
            fg=TEXT_COLOR,
            text="Пишите анекдот, а мы его продолжим!",
            font=FONT_BOLD,
            pady=10,
        )
        head_label.place(relwidth=1)

        # tiny divider
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        # text widget
        self.text_widget = Text(
            self.window,
            width=20,
            height=2,
            bg=BG_COLOR,
            fg=TEXT_COLOR,
            font=FONT,
            padx=5,
            pady=5,
        )
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # bottom label
        bottom_label = Label(self.window, bg=BG_GRAY, height=30)
        bottom_label.place(relwidth=1, rely=0.825)

        # message entry box
        self.msg_entry = Entry(bottom_label, bg= MESSAGE_ENTRY_BOX_COLOR, fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # send button
        send_button = Button(
            bottom_label,
            text="Отправить",
            font=FONT_BOLD,
            width=20,
            bg=BG_GRAY,
            command=lambda: self._on_enter_pressed(None),
        )
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

        # option models menu

        model_opt_list = ["Чужая модель", "Наша модель"]
        m_variable = StringVar(self.window)
        m_variable.set(model_opt_list[0])
        m_opt = OptionMenu(self.window, m_variable, *model_opt_list)
        m_opt.config(bg=BG_GRAY, font=FONT_BOLD)
        m_opt.place(relx=0.64, rely=0.9, relheight=0.06, relwidth=0.35)

        def m_callback(*args):
            self.mes_request.model_type = m_variable.get()
            if m_variable.get() == "Наша модель":
                create_tag_opt_list()
                self.mes_request.tag = "Еда"
            else:
                self.mes_request.tag = None
                tag_opt = Label(text="")
                tag_opt.config(bg=BG_GRAY, font=FONT_BOLD)
                tag_opt.place(relx=0.15, rely=0.9, relheight=0.06, relwidth=0.34)

        m_variable.trace("w", m_callback)

        # option length menu
        length_opt_list = [i for i in range(30, 110, 10)]
        l_variable = StringVar(self.window)
        l_variable.set(length_opt_list[0])
        l_opt = OptionMenu(self.window, l_variable, *length_opt_list)
        l_opt.config(bg=BG_GRAY, font=FONT_BOLD)
        l_opt.place(relx=0.50, rely=0.9, relheight=0.06, relwidth=0.14)

        def l_callback(*args):
            self.mes_request.length = int(l_variable.get())

        l_variable.trace("w", l_callback)

        # option tag menu

        def create_tag_opt_list():
            tag_opt_list = [
                "Еда",
                "Политика",
                "Коты",
                "Пошлые",
                "Про работу",
                "Компьютеры",
                "Дети",
                "Про Штирлица",
                "Про студентов",
                "Про соседей",
            ]
            tag_variable = StringVar(self.window)
            tag_variable.set(tag_opt_list[0])
            tag_opt = OptionMenu(self.window, tag_variable, *tag_opt_list)
            tag_opt.config(bg=BG_GRAY, font=FONT_BOLD)
            tag_opt.place(relx=0.15, rely=0.9, relheight=0.06, relwidth=0.34)

            def tag_callback(*args):
                self.mes_request.tag = tag_variable.get()

            tag_variable.trace("w", tag_callback)

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self.mes_request.text = msg
        self._insert_message(msg)

    def _insert_message(self, msg):
        if not msg:
            return

        self.msg_entry.delete(0, END)
        user_message = f"Затравка: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, user_message)
        self.text_widget.configure(state=DISABLED)

        message_from_model = f"Анекдот: {self.mes_request.process_request()}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, message_from_model)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)


if __name__ == "__main__":
    app = Application()
    app.run()
