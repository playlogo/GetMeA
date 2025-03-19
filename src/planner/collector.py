CAPTURE = ["NAME", "ID", "ID_LIKE", "VERSION"]


def get_linux_flavor():
    """Returns minified output similar to cat /etc/os-release"""

    res: list[str] = []

    with open("/etc/os-release", "r") as f:
        for line in f.readlines():
            if line.split("=")[0] in CAPTURE:
                res.append(line)

    return res
