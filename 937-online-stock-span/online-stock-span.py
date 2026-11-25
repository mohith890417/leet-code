class StockSpanner:

    def __init__(self):
        # Stack stores pairs of (price, span) in strictly decreasing price order
        self.stack = []

    def next(self, price: int) -> int:
        span = 1

        # Merge spans of previous consecutive days with price <= today's price
        while self.stack and self.stack[-1][0] <= price:
            _, prev_span = self.stack.pop()
            span += prev_span

        self.stack.append((price, span))
        return span