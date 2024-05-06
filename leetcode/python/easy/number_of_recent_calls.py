# task number - 933


class RecentCounter:
    def __init__(self):
        self.calls = []

    def ping(self, t: int) -> int:
        self.calls.append(t)
        while self.calls[0] < t - 3000:
            self.calls.pop(0)

        return len(self.calls)

    # def ping(self, t: int) -> int:
    #     self.calls.append(t)
    #     self.calls = [call for call in self.calls if t - 3000 <= call <= t]
    #     return len(self.calls)


if __name__ == '__main__':
    recent_counter = RecentCounter()
    print(recent_counter.ping(t=1))  # 1
    print(recent_counter.ping(t=100))  # 2
    print(recent_counter.ping(t=3001))  # 3
    print(recent_counter.ping(t=3002))  # 3
