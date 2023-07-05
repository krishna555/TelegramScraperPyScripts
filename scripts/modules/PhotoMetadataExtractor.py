from Utils import Utils

class PhotoMetadataExtractor:
	@staticmethod
	def getMetadata(message):
		photo_obj = message.media.photo
		photo_id = Utils.is_null_check(photo_obj.id),
		ttl_seconds = Utils.is_null_check(message.media.ttl_seconds)
		ts = photo_obj.date.isoformat() if photo_obj.date is not None else None
		# Utils.download_asset(self.client, photo_obj, str(photo_id), "jpg")
		return {
			"id": photo_id,
			"ts": ts,
			"ttl_seconds": ttl_seconds
		}