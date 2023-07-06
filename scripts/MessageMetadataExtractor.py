from telethon import TelegramClient, events, sync
from telethon.tl.types import InputPeerChat, InputPeerChannel, PeerChannel, PeerUser, PeerChat, MessageMediaPoll, MessageMediaWebPage, MessageMediaPhoto, MessageMediaDocument, Document, WebPage
import string
import random
import json
from modules.BaseMetadataExtractor import BaseMetadataExtractor
from modules.AssetMetadataExtractor import AssetMetadataExtractor
from modules.DocumentMetadataExtractor import DocumentMetadataExtractor
from modules.PhotoMetadataExtractor import PhotoMetadataExtractor
from modules.PollMetadataExtractor import PollMetadataExtractor
from modules.ReplyMetadataExtractor import ReplyMetadataExtractor
from modules.WebpageMetadataExtractor import WebpageMetadataExtractor
import os
import sys

class MessageMetadataExtractor:

	def __init__(self, api_id, api_hash, peer_channel_id, access_hash, min_id, max_id, output_path):
		self.api_id = api_id
		self.api_hash = api_hash
		self.client = None
		self.peer_channel_id = peer_channel_id
		self.access_hash = access_hash
		self.min_id = min_id
		self.max_id = max_id
		self.output_path = output_path

	def startClientSession(self):
		session_id = "test"
		self.client = TelegramClient(session_id, api_id=self.api_id, api_hash=self.api_hash)
		self.client.start()

	def get_messages(self):
		# print(type(self.peer_channel_id), type(self.access_hash), type(self.min_id), type(self.max_id))
		return self.client.get_messages(InputPeerChannel(self.peer_channel_id, self.access_hash), min_id=self.min_id, max_id=self.max_id)


	def extractMetadata(self, message):
		base_metadata = BaseMetadataExtractor.getMetadata(message)
		base_metadata["media_type"], base_metadata["media"] = AssetMetadataExtractor.getAssetMetadataForMsg(message)
		if base_metadata["reply_cnt"] > 0:
			base_metadata["replies"] = ReplyMetadataExtractor.getMetadata(self.client, InputPeerChannel(self.peer_channel_id, self.access_hash), message)
		return base_metadata

	def run(self):
		self.startClientSession()
		messages = self.get_messages()
		ans = []
		curr = 0


		if self.output_path and self.output_path[-1] == "/":
			self.output_path = self.output_path[:-1]

		of = open(self.output_path, "a")
		for (i, message) in enumerate(messages):
			json_line = json.dumps(self.extractMetadata(message)) + "\n"
			of.write(json_line)


if len(sys.argv) != 8:
	print("Run python3 MessageMetadataExtractor.py <API_ID> <API_HASH> <PEER_CHANNEL_ID> <ACCESS_HASH> <MIN_ID> <MAX_ID> <OUTPUT_PATH>")
	exit(1)


api_id = int(sys.argv[1])
api_hash = sys.argv[2]
peer_channel_id = int(sys.argv[3])
access_hash = int(sys.argv[4])
min_id = int(sys.argv[5])
max_id = int(sys.argv[6])
output_path = sys.argv[7] 


curr = 0
while curr < max_id:
	print(curr)
	msg_obj = MessageMetadataExtractor(api_id, api_hash, peer_channel_id, access_hash, curr, curr + 30, output_path)
	msg_obj.run()
	msg_obj.client.disconnect()
	curr += 29
# curr = 0
# while curr < 40000:
# 	print(curr)
# 	print()
# 	msg_obj = MessageMetadataExtractor(28331319, 'a3aea09bd36b94dafb6f3fd30d19f96a', 34765, 1777650412, 3992788351573039620, curr, curr + 30)
# 	msg_obj.run()
# 	msg_obj.client.disconnect()
# 	curr += 29