import argparse


def parse_args():
    """returns the parse arguments"""
    parser = argparse.ArgumentParser(description="A webscraper application")
    parser.add_argument("address", type=str, help="a web URL")
    parser.add_argument(
        "--screenshot", action="store_true", help="go to entered url and screenshot"
    )
    return parser.parse_args()
