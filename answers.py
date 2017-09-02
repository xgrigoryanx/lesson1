def get_answer(question):
	answers={"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
	return answers[question]
a=input("введите вопрос ")
print (get_answer(a))



