from Utils import Utils

class WebpageMetadataExtractor:
	@staticmethod
	def getMetadata(message):
		webpage_obj = message.media.webpage
		webpage_id = webpage_obj.id
		url = Utils.is_null_check(webpage_obj.url)
		webpage_type = Utils.is_null_check(webpage_obj.type)
		webpage_sitename = Utils.is_null_check(webpage_obj.site_name)
		title = Utils.is_null_check(webpage_obj.title)
		desc = Utils.is_null_check(webpage_obj.description)
		duration = Utils.is_null_check(webpage_obj.duration)

		# if webpage_obj.document is not None:
		# 	Utils.download_asset(self.client, webpage_obj.document, str(webpage_id), webpage_obj.document.mime_type.split("/")[-1])

		# if webpage_obj.photo is not None:
		# 	Utils.download_asset(self.client, webpage_obj.photo, str(webpage_id), "jpg")

		return {
			"id": webpage_id,
			"url": url,
			"type": webpage_type,
			"site_name": webpage_sitename,
			"title": title,
			"description": desc,
			"author": webpage_obj.author,
			"duration": duration
		}