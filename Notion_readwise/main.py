#!/usr/bin/env python3

from notion.client import NotionClient

with open("data.txt", "r") as f:
    token = f.read().splitlines()[0]
    link = "https://www.notion.so/2606f0ff4bcd47cebc1eed1a4c92581d?v=019319c195e7429a9484c84ad178df77"

client = NotionClient(token_v2=token)

cv = client.get_collection_view(link)

for row in cv.collection.get_rows():
    for block in row.children:
        color = block.get(path="format.block_color")
