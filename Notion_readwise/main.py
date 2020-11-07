#!/usr/bin/env python3

from notion.client import NotionClient
from notion.block import TextBlock
import time
import re

update_time = 180

with open("data.txt", "r") as f:
    data = f.read().split("\n")
    token = data[0]
    read_later_id = data[1]
    highlights_id = data[2]
    
client = NotionClient(token_v2=token)

read_later = client.get_collection_view(read_later_id)
highlights = client.get_collection_view(highlights_id)

def clean_text(text):
    output = re.sub(r"\[(.*?)\]\(.*?\)", r"\1", text)
    output = output.rstrip()
    return output

def update_highlights():
    highlight_rows = highlights.collection.get_rows()

    highlight_titles = [r.title for r in highlight_rows]

    for i, row in enumerate(read_later.collection.get_rows()):
        print("----------------------------------------------------")
        if row.title not in highlight_titles:
            added = highlights.collection.add_row()
            added.title = row.title
            highlight_rows = highlights.collection.get_rows()
            print("{}\n{}".format(added.title, highlight_rows[i].title))

        highlight_blocks = [clean_text(b.title) for b in highlight_rows[i].children]

        new_blocks = []

        for block in row.children:
            if block.type == "text":
                title = clean_text(block.title)
                if title not in highlight_blocks and block.get(path="format.block_color"):
                    new_blocks.append(title)

        print(highlight_blocks)
        print(new_blocks)

        page = highlight_rows[i]

        if highlight_blocks == [] and new_blocks == []:
            page.empty = True

        for block in new_blocks:
            new_block = page.children.add_new(TextBlock, title=block)
            page.empty = False
        print("Highlights updated")

update_highlights()
#while True:
#    update_highlights()
#    time.sleep(update_time)
