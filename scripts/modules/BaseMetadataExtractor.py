from telethon.tl.types import PeerChannel, PeerUser, PeerChat

class BaseMetadataExtractor:
	@staticmethod
	def getMetadata(message):
		peer_type = None

		peer_id = message.peer_id
		extracted_peer_id = None
		if type(peer_id) == PeerChannel:
			extracted_peer_id = peer_id.channel_id
			peer_type = peer_id.__class__.__name__
		elif type(peer_id) == PeerUser:
			extracted_peer_id = peer_id.user_id
			peer_type = peer_id.__class__.__name__
		elif type(peer_id) == PeerChat:
			extracted_peer_id = peer_id.PeerChat
			peer_type = peer_id.__class__.__name__

		reply_cnt = 0

		if message.replies is not None and message.replies.replies is not None:
			reply_cnt = message.replies.replies

		forwards_cnt = 0

		if message.forwards is not None:
			forwards_cnt = message.forwards

		res = {
			"id": message.id,
			"pinned": message.pinned,
			"edit_hide": message.edit_hide,
			"from_id": extracted_peer_id,
			"from_type": peer_type,
			"via_bot_id": message.via_bot_id,
			"forwards_cnt": message.forwards,
			"reply_cnt": reply_cnt,
			"views": message.views,
			"message": message.message,
			"date": message.date.isoformat()
		}

		if message.edit_date is not None:
			res["edit_date"] = message.edit_date.isoformat(),
		res["reactions"] = []
		if message.reactions is not None:
			for reaction in message.reactions.results:
				res["reactions"].append({
					"reaction": reaction.reaction,
					"count": reaction.count
					})

		if message.ttl_period is not None:
			res["ttl_period"] = message.ttl_period

		return res