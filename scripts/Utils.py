class Utils:
	@staticmethod
	def is_null_check(param):
		return param if param is not None else None

	@staticmethod
	def download_asset(self, client, asset, file_id, extension):
		self.client.download_media(asset, "assets/" + file_id + "." + extension)