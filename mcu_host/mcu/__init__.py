class DataStorage:
    def __init__(self):
        self._data = {}
        self._listeners = {}

    def update(self, k, v):
        self._data[k] = v
        self.notify(k)

    def get(self, k):
        if k in self._data:
            return self._data[k]

    def notify(self, k):
        if k not in self._listeners:
            return
        for listener in self._listeners[k]:
            listener(self._data[k])

    def register(self, k, callback):
        if k not in self._listeners:
            self._listeners[k] = [callback]
            return
        self._listeners[k].append(callback)

    def unregister(self, k, callback):
        if k not in self._listeners:
            return
        if callback in self._listeners[k]:
            self._listeners[k].remove(callback)


data_storage = DataStorage()
