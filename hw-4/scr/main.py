import argparse
from download import download_images_threaded, download_images_async

def main():
    parser = argparse.ArgumentParser(description="Download images from given URLs")
    parser.add_argument("urls", nargs="+", help="List of images URLs to download")
    parser.add_argument("--mode", choices=["threaded", "async"], default="threaded", help="Download mode: threaded (default) or async")
    args = parser.parse_args()

    if args.mode == "threaded":
        download_images_threaded(args.urls)
    elif args.mode == "async":
        import asyncio
        asyncio.run(download_images_async(args.urls))

if __name__ == "__main__":
    main()
