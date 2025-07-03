from googleapiclient.discovery import build
from isodate import parse_duration
import json
import pandas as pd
import os
from dotenv import load_dotenv

# --- Config ---
# replace this later with config/env handling
load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")
# fliptop channel id. This is generated with the help of a third party tool
CHANNEL_ID = "UCBdHwFIE4AJWSa3Wxdu7bAQ"


# --- Prepare output folder ---
os.makedirs("dataset", exist_ok=True)


# --- Initialize YouTube API client ---
# build() is used to construct the Youtube API service object
youtube = build("youtube", "v3", developerKey=API_KEY)


# --- Get uploads playlist id ---
channel_res = youtube.channels().list(
    part="contentDetails",  # to extract just the playlist info
    id=CHANNEL_ID
).execute()

uploads_playlist_id = channel_res["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
# print(f"Uploads Playlist ID: {uploads_playlist_id}")


# --- Collect video IDs from playlist ---
video_ids = []
next_page = None # used to navigate pages

while True:
    pl_response = youtube.playlistItems().list(
        part="snippet",
        playlistId=uploads_playlist_id,
        maxResults=50,
        pageToken=next_page
    ).execute()

    for item in pl_response["items"]:
        video_ids.append(item["snippet"]["resourceId"]["videoId"])

    next_page = pl_response.get("nextPageToken")
    if not next_page:
        break
    
# --- Fetch metadata
videos = []

for i in range(0, len(video_ids), 50):
    batch_ids = video_ids[i:i+50]

    vid_response = youtube.videos().list(
        part="snippet,statistics,contentDetails",
        id=",".join(batch_ids)
    ).execute()

    for item in vid_response["items"]:
        stats = item["statistics"]
        snippet = item["snippet"]
        content = item["contentDetails"]

        videos.append({
            "video_id": item["id"],
            "title": snippet["title"],
            "description": snippet["description"],
            "published_at": snippet["publishedAt"],
            "view_count": stats["viewCount"],
            "like_count": stats["likeCount"],
            "comment_count": stats["commentCount"],
            "video_duration": parse_duration(content["duration"]).total_seconds()
        })

'''
# Preview first 5 videos
for vid in videos[:3]:
    print(vid)
'''

# --- Save to a JSON file ---
with open("dataset/fliptop_videos.json", "w", encoding="utf-8") as f:
    json.dump(videos, f, ensure_ascii=False, indent=4)

# --- Save to csv file also ---
df = pd.DataFrame(videos)
df.to_csv("dataset/fliptop_videos.csv", index=False, encoding="utf-8")


print(f"✅ Done! Saved {len(videos)} videos to:")
print(f"Saved {len(videos)} videos to 'dataset/fliptop_videos.json'")
print(f"Saved {len(df)} videos to 'dataset/fliptop_videos.csv'")
