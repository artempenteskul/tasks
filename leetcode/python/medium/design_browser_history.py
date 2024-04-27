# task number - 1472


class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.pointer = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.pointer + 1] + [url]
        self.pointer = len(self.history) - 1

    def back(self, steps: int) -> str:
        self.pointer -= steps

        if self.pointer < 0:
            self.pointer = 0

        return self.history[self.pointer]

    def forward(self, steps: int) -> str:
        self.pointer += steps

        if self.pointer > len(self.history) - 1:
            self.pointer = len(self.history) - 1

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
