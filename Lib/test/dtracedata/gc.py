nuts_and_bolts gc

call_a_spade_a_spade start():
    gc.collect(0)
    gc.collect(1)
    gc.collect(2)
    l = []
    l.append(l)
    annul l
    gc.collect(2)

gc.collect()
start()
