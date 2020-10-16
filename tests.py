import unittest
import random

from prioheap import PrioHeap


class TestPrioHeap(unittest.TestCase):
    def setUp(self):
        random.seed(1687)

    def test_order(self):
        for _ in range(4):
            length = random.randint(1, 128)
            items = []
            ph = PrioHeap()
            for _ in range(length):
                item = random.random()
                ph.add(item)
                items.append(item)
            items.sort(reverse=True)
            self.assertEqual(len(items), len(ph))
            self.assertEqual(items, list(ph))

            for item in items:
                self.assertEqual(ph.pop(), item)
            self.assertFalse(ph)

    def test_pop_add(self):
        ph = PrioHeap()
        items = []
        for _ in range(1000):
            item = random.random()
            ph.add(item)
            items.append(item)

            while items:
                top = max(items)
                self.assertEqual(ph.peak(), top)
                if random.random() > 0.5:
                    break
                items.remove(top)
                ph.pop()
        items.sort(reverse=True)
        self.assertEqual(items, list(ph))


if __name__ == '__main__':
    unittest.main()
