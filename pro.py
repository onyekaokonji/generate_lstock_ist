import argparse

import numpy as np
import pandas as pd


def generator(df1: str, df2: str):
    """Function for generating new excel files using the
    similarities and dissimilarities between two files

    Parameters
    ----------
    df1 : first supply list - supplier's list

    df2 : second supply list - your list

    Returns
    -------
    two excel files.

    """
    df1 = pd.read_excel(df1)
    df2 = pd.read_excel(df2)

    dff1 = df1.iloc[:, 0].to_list()
    dff2 = df2.iloc[:, 0].to_list()

    set_a = set(dff1)
    set_b = set(dff2)

    intersection = set_a.intersection(set_b)
    diff = set_b - set_a

    common_items_list = list(intersection)
    uncommon_items_list = list(diff)

    common_items_dict = {"Name of item": common_items_list}
    uncommon_items_dict = {"Name of item": uncommon_items_list}

    new_df1 = pd.DataFrame(common_items_dict)
    new_df2 = pd.DataFrame(uncommon_items_dict)

    file_1 = new_df1.to_excel("file1.xlsx", index=False)
    file_2 = new_df2.to_excel("file2.xlsx", index=False)

    return file_1, file_2


parser = argparse.ArgumentParser(
    prog="procurement app",
    description="Generate new supply list for sending to a wholesaler",
    epilog="Thank you for using the procurement app!",
    add_help=False,
)
subparsers = parser.add_subparsers(title="subcommands")
arg_template = {
    "dest": "Files",
    "type": str,
    "nargs": 2,
    "help": "Path to your own list",
}

txn_parser = subparsers.add_parser("generator", help="Generate re-order lists")
txn_parser.add_argument(**arg_template)
parser.add_argument(
    "-v", "--version", action="version", version="%(prog)s version 0.1.0"
)
parser.add_argument(
    "-h",
    "--help",
    action="help",
    help="Enter path to wholesalers list before your list",
)
txn_parser.set_defaults(func=generator)

args = parser.parse_args()

args.func(*args.Files)
