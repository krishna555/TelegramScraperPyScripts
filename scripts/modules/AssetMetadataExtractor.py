from telethon.tl.types import MessageMediaPoll, MessageMediaWebPage, WebPage, MessageMediaPhoto, MessageMediaDocument

from modules.DocumentMetadataExtractor import DocumentMetadataExtractor
from modules.PhotoMetadataExtractor import PhotoMetadataExtractor
from modules.PollMetadataExtractor import PollMetadataExtractor
from modules.WebpageMetadataExtractor import WebpageMetadataExtractor

class AssetMetadataExtractor:
	@staticmethod
	def getAssetMetadataForMsg(message):
		media_obj = message.media
		class_name = media_obj.__class__.__name__
		if type(media_obj) == MessageMediaPoll:
			return (class_name, PollMetadataExtractor.getMetadata(message))
		elif type(media_obj) == MessageMediaWebPage and type(message.media.webpage) == WebPage:
			return (class_name, WebpageMetadataExtractor.getMetadata(message))
		elif type(media_obj) == MessageMediaPhoto:
			return (class_name, PhotoMetadataExtractor.getMetadata(message))
		elif type(media_obj) == MessageMediaDocument:
			return (class_name, DocumentMetadataExtractor.getMetadata(message))
		return (None, None)