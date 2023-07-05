from Utils import Utils

class DocumentMetadataExtractor:
	@staticmethod
	def getMetadata(message):
		doc_obj = message.media.document
		doc_id = Utils.is_null_check(doc_obj.id)
		mime_type = Utils.is_null_check(doc_obj.mime_type)
		size = Utils.is_null_check(doc_obj.size)
		ttl_seconds = Utils.is_null_check(message.media.ttl_seconds) 

		# Utils.download_asset(self.client, doc_obj, str(doc_id), doc_obj.mime_type.split("/")[-1])
		return {
			"id": doc_id,
			"mime_type": mime_type,
			"size": size,
			"ttl_seconds": ttl_seconds
		}