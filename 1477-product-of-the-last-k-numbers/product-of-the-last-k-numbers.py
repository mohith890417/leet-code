class ProductOfNumbers:
    def __init__(self):
        # Sentinel 1 simplifies prefix division; reset to [1] whenever 0 arrives.
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        # If k reaches or passes the last reset point, a 0 is inside the last k numbers.
        if k >= len(self.prefix):
            return 0
        return self.prefix[-1] // self.prefix[-1 - k]