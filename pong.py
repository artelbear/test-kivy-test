# Game pong


def init():
    from kivy.app import App
    from kivy.uix.widget import Widget

    class PongGame(Widget):
        pass

    class PongApp(App):
        def build(self):
            return PongGame()

    print("run")
    PongApp().run()
    print("exit")


if __name__ == "__main__":
    print("pong.py is main")
    init()
