"""
This module processes a feed, checks if the feed's GUID exists in an Azure Table, posts new entries to Twitter, and stores them in the Azure Table.
"""

import os
import logging
import datetime
import feedparser
import tweepy
from azure.data.tables import TableServiceClient
from azure.core.exceptions import ResourceNotFoundError, HttpResponseError
import datetime
from twitter_client import client


def process_feed(feed_url):
    """
    Processes a feed from a given URL and returns a list of recent entries.

    Parameters:
    feed_url (str): The URL of the feed to be processed.

    Returns:
    list: A list of dictionaries, each representing a recent entry from the feed. 
          Each dictionary contains the title, link, summary, guid, and published_date of the entry.
          If an error occurs during processing, an empty list is returned.
    """
    try:
        feed = feedparser.parse(feed_url)
        cutoff_time = datetime.datetime.now() - datetime.timedelta(hours=12)

        recent_entries = []
        for entry in feed.entries:
            published_tuple = entry.published_parsed
            published_date = datetime.datetime(*published_tuple[:6])
            if published_date >= cutoff_time:
                entry_details = {
                    "title": entry.title,
                    "link": entry.link,
                    "summary": entry.summary,
                    "guid": entry.id,
                    "published_date": published_date
                }
                recent_entries.append(entry_details)

        return recent_entries
    except Exception as e:
        logging.error(f"Error processing feed: {e}")
        return []


def check_guid_in_table(guid):
    """
    Checks if the GUID exists in the Azure Table.

    Parameters:
    guid (str): The GUID to check.

    Returns:
    bool: True if the GUID exists in the table, False otherwise.
    """
    try:
        table_service_client = TableServiceClient.from_connection_string(os.getenv("CONNECTION_STRING"))
        table_client = table_service_client.get_table_client(table_name=os.getenv("TABLE_NAME"))
        table_client.get_entity(partition_key="PartitionKey", row_key=guid)
        return True  
    except ResourceNotFoundError:
        return False
    except HttpResponseError as e:
        logging.error(f"Error accessing Azure Table Storage: {e}")
        return False

def post_to_twitter_and_store(today_entries):

    """
    Posts new entries to Twitter and stores them in the Azure Table.

    Parameters:
    today_entries (list): A list of dictionaries containing details of each entry from today.
    """
    try:
        table_service_client = TableServiceClient.from_connection_string(os.getenv("CONNECTION_STRING"))
        table_client = table_service_client.get_table_client(table_name=os.getenv("TABLE_NAME"))

        for entry in today_entries:
            title = entry["title"]
            link = entry["link"]
            summary = entry["summary"]
            guid = entry["guid"]
            published_date = entry["published_date"]

            if not check_guid_in_table(guid):
                tweet_text = f"{title}\n\n{summary}\n\n{link}"
                if len(tweet_text) > 280:
                    max_summary_length = 280 - (len(title) + len(link) + 4)
                    trimmed_summary = summary[:max_summary_length]
                    tweet_text = f"{title}\n\n{trimmed_summary}\n\n{link}"
                
                try:
                    client.create_tweet(text=tweet_text)
                    logging.info(f"Tweet posted for {title}")
                except tweepy.TweepyException as e:
                    logging.error(f"Error posting tweet: {e}")
                    continue

                try:
                    table_client.upsert_entity(
                        entity={
                            "PartitionKey": "PartitionKey",
                            "RowKey": guid,
                            "Title": title,
                            "Link": link,
                            "Summary": summary,
                            "PublishedDate": published_date.strftime("%Y-%m-%d %H:%M:%S")
                        }
                    )
                    logging.info(f"Entry added to Azure Table Storage for {title}")
                except HttpResponseError as e:
                    logging.error(f"Error storing entry in Azure Table Storage: {e}")
            else:
                logging.info(f"Skipping tweet and storage for {title} as GUID exists in table")
    except Exception as e:
        logging.error(f"Error in post_to_twitter_and_store: {e}")
        

def main():
    """
    Gets the feed URL from an environment variable, processes the feed, and posts new entries to Twitter and stores them in the Azure Table.
    """
    feed_url = os.getenv("FEED_URL")
    yesterdays_entries = process_feed(feed_url)
    post_to_twitter_and_store(yesterdays_entries)
