

class History:
    def __init__(self):
        self.history = []
        self.history_pos = 0

    def add(self, snapshot):
        if not snapshot:
            return
        if self.history_pos == len(self.history) - 1:
            self.history.append(snapshot)
            self.history_pos = len(self.history) - 1
        else:
            pos = 0
            if self.undo_available:
                pos = self.history_pos + len(snapshot)
            self.history = self.history[:pos]

            self.history.append(snapshot)
            self.history_pos = len(self.history) - 1

    @property
    def undo_available(self):
        return bool(self.history[:self.history_pos])

    @property
    def redo_available(self):
        return bool(len(self.history) - 1 - self.history_pos)

    def _get(self, position):
        return self.history[position]

    def undo(self):
        if self.history_pos >= 1:
            self.history_pos -= 1

        pos = self.history_pos
        snap = self._get(pos)


        return snap

    def redo(self):
        pos = self.history_pos + 1

        if pos >= len(self.history):
            pos = len(self.history) - 1

        snap = self._get(pos)
        if self.history_pos < len(self.history) - 1:
            self.history_pos += 1

        return snap


if __name__ == '__main__':
    h = History()
    h.add({0:True})
    h.add({1:True})
    h.add({2:True})
    h.add({3:True})
    h.add({4:True})
    print(h.history)
    for i in range(2):
        print('undo', h.undo())
    # h.add({4:True})
    # print(h.history_pos, h.history)
    for i in range(2):
        print('redo', h.redo())


    # print(h.history)