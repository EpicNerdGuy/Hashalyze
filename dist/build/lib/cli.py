import argparse
from main import check_hash

def run_cli():
    parser = argparse.ArgumentParser(description="Hash Identifier CLI Tool")
    parser.add_argument("--hash", required=True, help="Hash to identify")
    parser.add_argument("--format", choices=["text", "json"], default="text")

    args = parser.parse_args()
    result = check_hash(args.hash)

    if args.format == "json":
        import json
        print(json.dumps(result, indent=2))
    else:
        print(result)

if __name__ == "__main__":
    run_cli()
