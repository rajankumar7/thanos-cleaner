import argparse
from .thanos import snap
from . import __app_name__, __version__

def get_args() -> argparse.Namespace:
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "-target",
        "--target",
        help="path to directory from where files need to be cleaned.",
        required=True,
    )
    
    argparser.add_argument(
        "-v",
        "--version",
        action="version",
        version=__app_name__ + ":" + __version__,
    )

    return argparser.parse_args()



if __name__ == "__main__":
    user_inputs = get_args()
    snap(user_inputs)