"""Console script for vaqc."""
import argparse
import sys
from pathlib import Path
from .vaqc import process_fmriprep


def main():
    """Console script for vaqc."""
    parser = argparse.ArgumentParser()
    parser.add_argument('derivatives_dir',
                        type=Path,
                        action='store',
                        help='the root folder of a BIDS derivative dataset '
                        '(sub-XXXXX folders '
                        'should be found at the top level in this folder).')
    args = parser.parse_args()
    print("using input directory as ", args.derivatives_dir)

    if args.derivatives_dir.name == 'fmriprep':
        process_fmriprep(args.derivatives_dir)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
