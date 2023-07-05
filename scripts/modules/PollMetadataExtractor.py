from Utils import Utils

class PollMetadataExtractor:
	@staticmethod
	def getMetadata(message):
		poll_obj = message.media.poll
		poll_id = poll_obj.id
		question = poll_obj.question
		answers = poll_obj.answers
		message_media_poll_results = message.media.results
		res = []
		for answer in answers:
			res.append({
					"text": Utils.is_null_check(answer.text),
					"option": int(answer.option)
				})

		# Extract Results:
		# https://tl.telethon.dev/constructors/poll_results.html
		poll_end_stats = []
		if message_media_poll_results is not None and message_media_poll_results.results is not None:
			for poll_answer_voters in message_media_poll_results.results:
				poll_end_stats.append({
						"option": int(poll_answer_voters.option),
						"count": int(poll_answer_voters.voters)
					})
		total_voters = Utils.is_null_check(message_media_poll_results.total_voters)
		solution = Utils.is_null_check(message_media_poll_results.solution)
		closed = Utils.is_null_check(poll_obj.closed)
		public_voters = Utils.is_null_check(poll_obj.public_voters)
		multiple_choice = Utils.is_null_check(poll_obj.multiple_choice)
		quiz = Utils.is_null_check(poll_obj.quiz)
		close_date = poll_obj.close_date.isoformat() if poll_obj.close_date is not None else None

		return {
			"id": poll_id,
			"question": question,
			"answers": res,
			"closed": closed,
			"public_voters": public_voters,
			"multiple_choice": multiple_choice,
			"quiz": quiz,
			"poll_stats": poll_end_stats,
			"close_date": close_date,
			"total_voters": total_voters,
			"solution": solution
		}