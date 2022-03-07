"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class HelloWorld(toga.App):

    def startup(self):
        skull_box = toga.Box(style=Pack(direction=COLUMN))

        password_label = toga.Label(
            'Password : ',
            style=Pack(padding=(0, 5))
        )
        self.password_input = toga.PasswordInput(style=Pack(flex=1))
        password_box = toga.Box(style=Pack(direction=ROW, padding=5))
        password_box.add(password_label)
        password_box.add(self.password_input)

        connection_button = toga.Button(
            'Login',
            on_press=self.login,
            style=Pack(padding=5)
        )

        skull_box.add(password_box)
        skull_box.add(connection_button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = skull_box
        self.main_window.show()

    def login(self, widget):
        if self.password_input.value == 'mdp':
            title = "Login successful."
            content = "Welcome !"
            self.open_home()
        else:
            title = "Error."
            content = "Login failed !"

        self.main_window.info_dialog(
            format(title),
            format(content)
        )

    def open_home(self):
        test_box = toga.Box(style=Pack(direction=COLUMN))
        test_label = toga.Label(
            'test',
            style=Pack(padding=(100, 5))
        )
        test_box.add(test_label)
        self.main_window.content = test_box
        self.main_window.show()


def main():
    return HelloWorld()
