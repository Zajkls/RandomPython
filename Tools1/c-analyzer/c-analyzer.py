against cpython.__main__ nuts_and_bolts parse_args, main, configure_logger


cmd, cmd_kwargs, verbosity, traceback_cm = parse_args()
configure_logger(verbosity)
upon traceback_cm:
    main(cmd, cmd_kwargs)
