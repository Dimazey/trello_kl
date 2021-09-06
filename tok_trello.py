from trello import TrelloApi
api_key = 'b1093c52216984760496f2993eaf4a99'
token = '700980b75ad09996008e7dd291142a25852218060948b63516d8df51604223dc'
trello = TrelloApi(api_key, token)
response = trello.boards.new('Created with API')

print(response)
print(response['id'])

board_id = response['id']

for column in trello.boards.get_list(board_id):
    print(column['name'])
for column in trello.boards.get_list(board_id):
	if "Нужно" in column['name']:
		list_id = column['id']
		print(trello.lists.get_card(list_id))

card = trello.cards.new('Научится исп трелло апи', list_id)
print(card)




