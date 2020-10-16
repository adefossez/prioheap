class PrioHeap:
    """
    Binary-tree based priority queue.
    Items should support comparison, use tuples if score != value.
    Add items with .add(...)
    At any point in time you can peak element with highest score
    """
    def __init__(self):
        self._storage = []

    def __len__(self):
        return len(self._storage)

    def __bool__(self):
        return bool(self._storage)

    def __repr__(self):
        return "HeapQ({})".format(repr(list(self)))

    def __iter__(self):
        if not self:
            return
        bfs = PrioHeap()
        bfs.add((self.peak(), 0))
        while bfs:
            item, index = bfs.pop()
            yield item
            for child in [2 * index + 1, 2 * index + 2]:
                if child < len(self):
                    bfs.add((self._storage[child], child))

    def add(self, item):
        index = len(self._storage)
        self._storage.append(item)
        while index > 0:
            item = self._storage[index]
            pindex = (index - 1) // 2
            parent = self._storage[pindex]
            if item > parent:
                self._storage[index] = parent
                self._storage[pindex] = item
                index = pindex
            else:
                break

    def peak(self):
        if not self:
            raise IndexError("Empty HeapQ")
        return self._storage[0]

    def pop(self):
        if not self:
            raise IndexError("Empty HeapQ")
        peak = self._storage[0]
        if len(self) == 1:
            self._storage.pop()
        elif len(self) >= 2:
            self._storage[0] = self._storage.pop(-1)
            index = 0
            while index < len(self):
                item = self._storage[index]
                top_item = item
                top_index = index
                for child in [2 * index + 1, 2 * index + 2]:
                    if child < len(self):
                        citem = self._storage[child]
                        if citem > top_item:
                            top_item = citem
                            top_index = child
                if top_index == index:
                    break
                self._storage[index] = top_item
                self._storage[top_index] = item
                index = top_index
        return peak
