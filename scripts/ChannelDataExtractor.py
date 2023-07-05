
from telethon import TelegramClient, events, sync
from telethon.tl.types import Channel, MessageMediaPhoto, MessageMediaDocument
import json
from Utils import Utils
import sys


class ChannelMetadataExtractor:

	def __init__(self, api_id, api_hash):
		self.api_id = api_id
		self.api_hash = api_hash
		self.client = TelegramClient("ChannelMetadataExtractor", api_id=api_id, api_hash=api_hash)

	def getChannelMetadataFromDialog(self, dialog):

		name = dialog.name 
		peer_channel_id = dialog.entity.id 
		access_hash = dialog.entity.access_hash
		title = dialog.entity.title
		description = dialog.message.message
		participants_cnt = dialog.entity.participants_count
		user_name = dialog.entity.username

		# media_obj = dialog.message.media

		# if type(media_obj) == MessageMediaPhoto:
		# 	photo_id = media_obj.photo.id
		# elif type(media_obj) == MessageMediaDocument:
		# 	photo_id = media_obj.document.id

		# if photo_id is not None:
		# 	Utils.download_media(self.client, media_obj, f"../outputs/channelAssets/{photo_id}.jpg")
		return {
			"name": name,
			"peer_channel_id": peer_channel_id,
			"access_hash": access_hash,
			"title": title,
			"description": description,
			"participants_cnt": participants_cnt,
			"user_name": user_name
		}

	def run(self):
		self.client.start()

		extracted_data = []
		for dialog in self.client.get_dialogs():

			if type(dialog.entity) == Channel:
				extracted_data.append(self.getChannelMetadataFromDialog(dialog))


		with open("../outputs/ChannelMetadata.txt", "w") as of:
			json.dump(extracted_data, of)

if len(sys.argv) != 3:
	print("Run python3 ChannelMetadataExtractor <API_ID> <API_HASH>")
	exit(1)

api_id = int(sys.argv[1])
api_hash = sys.argv[2]
obj = ChannelMetadataExtractor(api_id, api_hash)
obj.run()