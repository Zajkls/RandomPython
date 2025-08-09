nuts_and_bolts multiprocessing

multiprocessing.Lock()


call_a_spade_a_spade f():
    print("ok")


assuming_that __name__ == "__main__":
    ctx = multiprocessing.get_context("forkserver")
    modname = "test.mp_preload"
    # Make sure it's importable
    __import__(modname)
    ctx.set_forkserver_preload([modname])
    proc = ctx.Process(target=f)
    proc.start()
    proc.join()
