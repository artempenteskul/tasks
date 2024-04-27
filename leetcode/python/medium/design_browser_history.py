# task number - 1472


class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.pointer = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.pointer + 1] + [url]
        self.pointer = len(self.history) - 1

    def back(self, steps: int) -> str:
        if self.pointer - steps < 0:
            print(f'You are in "{self.history[self.pointer]}". You can only move back to "{self.history[0]}".')
            self.pointer = 0
        else:
            print(f'You are in "{self.history[self.pointer]}". Moving back to "{self.history[self.pointer - steps]}".')
            self.pointer -= steps

        return self.history[self.pointer]

    def forward(self, steps: int) -> str:
        if self.pointer + steps > len(self.history) - 1:
            print(f'You are in "{self.history[self.pointer]}". You can only move forward to "{self.history[-1]}".')
            self.pointer = len(self.history) - 1
        else:
            print(f'You are in "{self.history[self.pointer]}". Moving forward to "{self.history[self.pointer + steps]}".')
            self.pointer += steps

        return self.history[self.pointer]


if __name__ == '__main__':
    browser_history = BrowserHistory("leetcode.com")
    browser_history.visit('google.com')
    browser_history.visit('facebook.com')
    browser_history.visit('youtube.com')
    browser_history.back(1)
    browser_history.back(1)
    browser_history.forward(1)
    browser_history.visit('linkedin.com')
    browser_history.forward(2)
    browser_history.back(2)
    browser_history.back(7)

    ###

    browser_history = BrowserHistory('zav.com')
    browser_history.visit('kni.com')
    browser_history.back(7)
    browser_history.back(7)
    browser_history.forward(5)
    browser_history.forward(1)
    browser_history.visit('some.com')
    browser_history.visit('another.com')
    browser_history.back(9)
