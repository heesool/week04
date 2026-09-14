import argparse


def non_whitespace_name(value: str) -> str:
    if not value.strip():
        raise argparse.ArgumentTypeError("name must not be blank")
    return value.strip()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True, type=non_whitespace_name)
    args = parser.parse_args()
    print(f"Hello, {args.name}!")


if __name__ == "__main__":
    main()
