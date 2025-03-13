from args import args, parser
from setup import setup, update
from handler import run

# Entrypoint
if __name__ == "__main__":
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
