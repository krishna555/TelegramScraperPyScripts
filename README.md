# Overview

This repository contains scripts to extract messages from Telegram channels using Telethon.


## Metadata Structure:


1. Message Object:
```
{
	"id": "(Integer) Id of the Message",
	"pinned": "(Boolean) Was the message pinned",
	"edit_hide": "(Boolean) Is the Edit Hide Status hidden",
	"from_id": "(Integer) Id of the Sender",
	"from_type": "(Integer) Sender Type - PeerChannel, PeerUser, PeerChat",
	"via_bot_id": "(Integer) Bot Id if the message was sent by a bot on the channel",
	"forwards_cnt": "(Integer) Number of times the message was forwarded.",
	"reply_cnt": "(Integer) Number of replies to the message",
	"views": "(Integer) Number of views to the message",
	"message": "(String) Message Text",
	"date": "(String) Date in ISO Format, can be converted to date object using fromisoformat Python API",
	"edit_date": "(String) Latest Edit Date of the message in ISO Format."
	"media": "(Object) Object containing any media asset attached to the message",
	"media_type": "(String) Media asset type values - "MessageMediaPoll", "MessageMediaWebPage", "MessageMediaPhoto", "MessageMediaDocument""
	"reactions": {
		"reaction": "(String) Reaction",
		"count": : "(Integer) Number of users upvoting the reaction"
	},
	"ttl_period": "(Integer) TTL Period of the message",
	"replies": "(List<Message>) List of Replies to original message."
}
```


2. Asset Type:


1. MessageMediaPoll Type:

   1. Reference: 

      1. [https://tl.telethon.dev/constructors/message_media_poll.html](https://tl.telethon.dev/constructors/message_media_poll.html)
      2. [https://tl.telethon.dev/constructors/poll.html](https://tl.telethon.dev/constructors/poll.html)
      3. [https://tl.telethon.dev/types/poll_results.html](https://tl.telethon.dev/types/poll_results.html)
      4. [https://tl.telethon.dev/constructors/poll_answer_voters.html](https://tl.telethon.dev/constructors/poll_answer_voters.html)

```
{
	"id": "(Integer) Id of the Poll",
	"question": "(String) Question of the Poll",
	"answers": {
		"text": "(String) Poll Text",
		"option": "(Integer) Option Number"
	},
	"closed": "(Boolean) Is the Poll closed?",
	"public_voters": "(Boolean)",
	"multiple_choice": "(Boolean)",
	"quiz": "(Boolean)",
	"close_date": "(Int)",
	"total_voters": "(Integer) Total number of voters.",
	"solution": "(String)"
} 
```

2. MessageMediaWebPage

   1. Reference: 

      1. [https://tl.telethon.dev/constructors/message_media_web_page.html](https://tl.telethon.dev/constructors/message_media_web_page.html)
      2. [https://tl.telethon.dev/constructors/web_page.html](https://tl.telethon.dev/constructors/web_page.html)


```
{
	"id": "(Integer) Webpage Id",
	"url": "(String) URL of the webpage",
	"type": "(String) Webpage Type",
	"site_name": "(String) Webpage Site Name",
	"title": "(String) Webpage Title",
	"descirption": "(String) Webpage Description",
	"author": "(String) Author of the message",
	"duration": "(Integer)"
}
```


3. MessageMediaPhoto

   1. Reference: 

      1. [https://tl.telethon.dev/constructors/message_media_photo.html](https://tl.telethon.dev/constructors/message_media_photo.html)
      2. [https://tl.telethon.dev/constructors/photo.html](https://tl.telethon.dev/constructors/photo.html)

```
{
	"id": "(Integer) Id of the message",
	"ts": "(String) ISO Format Date String,
	"ttl_seconds": "(Integer) TTL for the photo"
}
```

4. MessageMediaDocument

   1. Reference: 

      1. [https://tl.telethon.dev/constructors/message_media_document.html](https://tl.telethon.dev/constructors/message_media_document.html)
      2. [https://tl.telethon.dev/constructors/document.html](https://tl.telethon.dev/constructors/document.html)

```
{
	"id": "(Integer) Document Id",
	"mime_type": "(String) Document Mime Type",
	"size": "(Integer) Document Size",
	"ttl_seconds": "(Integer) TTL for the document"
}
```


## Setup:

1. **Retrieve API_ID and API_HASH:** We need an API_ID and API_HASH to interact with the Telegram API. Follow the steps in [Obtaining api_id section](https://core.telegram.org/api/obtaining_api_id#obtaining-api-id).
2. **Identify which channels are to be scraped:** Run `ChannelDataExtractor.py` with the following command: `python3 ChannelDataExtractor.py <API_ID> <API_HASH>`. The output is stored in `outputs/ChannelMetadata.txt` file. Use a JSON Viewer to look at available channels to be scraped.
	Each channel's metadata has the following structure:

	```
	{
		"name": "(String) Name of the channel",
		"peer_channel_id": "(Integer) Peer Channel Id of the channel",
		"access_hash": "(Integer) Access Hash of the channel",
		"title": "(String) Title of the channel",
		"description": "(String) Description of the channel",
		"participants_cnt": "(Integer) Number of participants",
		"user_name": "(String) Channel User name"
	}
	```

	We need the `peer_channel_id` and `access_hash` in the next steps of scraping.

3. **Extract Metadata**: Run `python3 MessageMetadataExtractor.py <API_ID> <API_HASH> <PEER_CHANNEL_ID> <ACCESS_HASH> <MIN_ID> <MAX_ID> <OUTPUT_PATH>`.
   1. `<API_ID>` and `<API_HASH>` were obtained from step 1.
   2. `<PEER_CHANNEL_ID>` and `<ACCESS_HASH>` were obtained from step 2.
   3. Every message in a channel has an id which can be found in the URL. For example, when you navigate to the web version of telegram `web.telegram.com`, login, navigate to a channel, right click on a message and copy its link. The link will be of the form, `https://t.me/<group_name>/<message_id>`. We can extract messages that lie within a range of message_ids. Usually messages go from 1 up to the last message id of the channel.
   4. `<MIN_ID>` - all messages lesser than `MIN_ID` will be ignored, `<MAX_ID>` - all messages greater than `MAX_ID` will be ignored.
   5. `<OUTPUT_PATH>` - Output metadata file where each line is a JSON corresponding to a message.