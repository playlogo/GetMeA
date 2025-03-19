from args import ArgsType

from planner.planner import Planner

import asyncio


def run(args: ArgsType):
    if len(args["args"]) != 1:
        print("Currently only one installation at once supported!")
        exit(-1)

    asyncio.run(install(args["args"][0]))


async def install(program: str):
    # Create handler and try to create plan
    handler = Planner()
    plan = await handler.plan(program)

    # Format & Print plan, wait for confirmation
    confirmation = await plan.print_confirmation()

    if not confirmation:
        print("Exiting")
        exit(-1)

    # Install
    success, error = await plan.execute()

    if success:

        print(f"\rDone! Successfully installed {plan.name}")
    else:
        print(f"\rThere was a error: " + error)
        exit(-1)
