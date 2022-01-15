import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input-csv", help="Tab separated file with one URL and ID per line to check.", required=True,
    )
    parser.add_argument(
        "--output-folder", help="Folder where to save the results, one folder per URL", required=True,
    )
    parser.add_argument(
        "--output-csv", help="Tab separated file containing the results of the check", required=True,
    )
    parser.add_argument("--proxy-server", help="If we are behind a proxy (without authentication)")

    args = parser.parse_args()


if __name__ == "__main__":
    main()
