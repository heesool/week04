import sys


def parse_version(version):
    return tuple(int(part) for part in version.split("."))


def is_compatible(current, candidate):
    current_version = parse_version(current)
    candidate_version = parse_version(candidate)

    return (
        current_version[0] == candidate_version[0]
        and candidate_version >= current_version
    )


if __name__ == "__main__":
    current = sys.argv[1]
    candidate = sys.argv[2]

    if is_compatible(current, candidate):
        print("compatible")
    else:
        print("incompatible")
