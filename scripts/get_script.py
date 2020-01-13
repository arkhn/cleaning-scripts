import re
from scripts import custom
from scripts import logic
from scripts import utils

functions = {}


def get_script(name):
    if name in custom.__all__:
        return getattr(custom, name)
    elif name in utils.__all__:
        return getattr(utils, name)
    else:
        if name.startswith("if_valid("):
            # get args part between (  )
            args_part = name[name.find("(") + 1 : name.rfind(")")]  # noqa
            args = re.split(", |,", args_part)
            for i, arg in enumerate(args):
                if arg in custom.__all__:  # if custom function
                    args[i] = getattr(custom, arg)
                elif arg in utils.__all__:  # if utility function
                    args[i] = getattr(utils, arg)
                elif re.match(r'^".*"$', arg) or re.match(
                    r"^'.*'$", arg
                ):  # if string "..." '...'
                    args[i] = arg[1:-1]
                elif arg.replace(".", "", 1).isdigit():  # if number
                    args[i] = arg
                else:
                    raise ValueError(f"Argument {arg} not recognised")
            print(args)
            return logic.if_valid(*args)
        else:
            raise NameError("Function", name, "not found.")
