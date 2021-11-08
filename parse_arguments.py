import argparse


def parse_args():
    """returns the parse arguments"""
    parser = argparse.ArgumentParser(description="A webscraper application")
    parser.add_argument("item", type=str, help="item to be searched for")
    parser.add_argument("--screenshot", action="store_true", help="take a screenshot")
    # parser.add_argument(
    #      "--test", type=int, help="store nums"
    # )
    # parser.add_argument(
    #      "--test2", type=str, help="store string"
    # )
    return parser.parse_args()
