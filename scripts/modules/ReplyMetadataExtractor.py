from modules.BaseMetadataExtractor import BaseMetadataExtractor
from modules.AssetMetadataExtractor import AssetMetadataExtractor

class ReplyMetadataExtractor:

	@staticmethod
	def getMetadata(client, peer_obj, message):
		replies = client.iter_messages(peer_obj, reply_to=message.id)
		
		extracted_data = []
		for reply in replies:
			base_metadata = BaseMetadataExtractor.getMetadata(reply)
			base_metadata["asset"] = AssetMetadataExtractor.getAssetMetadataForMsg(reply)

			extracted_data.append(base_metadata)

		return extracted_data