def my_message(message):
	message = message
	def second_func(answer):
		answer = answer	
		print(message, answer)	
	return second_func

answer = 42
message = "Your answer is: "

correct_answer_is = my_message(message)
correct_answer_is(answer)
