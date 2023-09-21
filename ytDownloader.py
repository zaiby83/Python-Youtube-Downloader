import certifi
import ssl
from pytube import YouTube
import sys

# Set the certificate authority file
ssl._create_default_https_context = ssl._create_unverified_context
ssl._create_default_https_context().load_verify_locations(certifi.where())

# Check if the command-line argument is provided
if len(sys.argv) < 2:
    print("Usage: python script.py <YouTube URL>")
    sys.exit(1)

# Get the YouTube URL from the command-line argument
link = sys.argv[1]

try:
    yt = YouTube(link)
except Exception as e:
    print("Error:", e)
    sys.exit(1)

print("Title:", yt.title)
print("Views:", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download('/Users/a./Downloads/Projects/PyTube Downloader/Downloaded Videos')