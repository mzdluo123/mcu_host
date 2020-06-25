from mcu_host.mcu import DataStorage

data = DataStorage()

callback = lambda x: print(f"l is update to {x}")
data.update("l", 1)
data.register("l", callback)
data.update("l", 2)
data.update("x", 2)
data.unregister("l", callback)
data.update("l", 3)