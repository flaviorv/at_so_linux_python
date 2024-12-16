from random import randrange
import asyncio

number = None

async def generator(drawed):
	global number
	await asyncio.sleep(1)
	_number = randrange(1, 101)
	while _number in drawed:
		_number = randrange(1, 101)
	drawed.append(_number)
	number = _number

async def narrator(event):
	global number
	await asyncio.sleep(1)
	while number == None:
		await asyncio.sleep(1)
	print(f"Number is {number}")
	event.set()

async def player(event, players_list):
	await asyncio.sleep(1)
	while event.is_set() == False:
		await asyncio.sleep(2)
	global number
	for _player in players_list:
		name = _player[0]
		card = _player[1]
		checking_card = _player[3]
		if number in card and number not in checking_card:
	    		_player[3].append(number)
	    		checking_card = _player[3]
		if len(checking_card) < len(card):
	    		print(f"{name} {number} {card} {len(checking_card)}")
		else:
	    		print(f"{name} is the WINNER {card} {checking_card}")
	    		return "Winner"

async def main():
	players_list = [
		["player-1", [5,10,48,55],0, []],
		["player-2", [8,46,80,99],0, []],
		["player-3", [17,29,78,95],0, []]
	]

	drawed_numbers = []

	count = 0
	while count < 100:
		count += 1
		event = asyncio.Event()
		result = await asyncio.gather(*[generator(drawed_numbers), narrator(event), player(event, players_list)])
		if result[2] == "Winner":
			break
	print("Game is Over")

asyncio.run(main())
