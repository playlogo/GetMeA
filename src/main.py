from args import args, parser
from setup import setup, update
from planner.handler import run


from sys import platform


# Entrypoint
if __name__ == "__main__":
    if platform != "linux" and platform != "linux2":
        # Currently only supported on linux (due to the nature of a linux package installation tool...)
        print("GetMeA currently only support linux")
        exit(-1)

    if len(args["args"]) == 0:
        parser.print_usage()
        exit(-1)

    if len(args["args"]) == 1 and "setup" in args["args"]:
        # Initial setup
        setup(args)
    elif len(args["args"]) == 1 and "update" in args["args"]:
        # Initial setup
        update(args)
    else:
        # Software installation
        run(args)
