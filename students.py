import json
from concurrent.futures import Future, ThreadPoolExecutor, TimeoutError
import threading
import time
from multiprocessing import Process


def get_student(enrollment):
	future = Future()
	with open("data.json", "r") as file:
		data = json.load(file)
		student = data[enrollment]
	timer = threading.Timer(3, lambda: future.set_result(student))
	timer.start()
	return future

average_grade = 0
students = 0
grades_sum = 0
def get_record_by_id(enrollment, process):
	fut = get_student(enrollment)
	def on_done_future(future):
		student = future.result()
		if student != None:
			global average_grade
			global students
			global grades_sum
			grades_sum += student[1]
			students += 1
			average_grade = grades_sum/students
			print(f"Aluno: {student[0]} - Nota: {student[1]} - Nota média da turma: {"%.2f" % average_grade}")
			process.terminate()
			return
		print(f"Matrícula não existe")
	fut.add_done_callback(on_done_future)

def get_all_records():
	time.sleep(30)
	with open("data.json", "r") as file:
		data = json.load(file)
		students = data
	return students

def runner():
	print(get_all_records())

process = Process(target=runner)
process.start()
get_record_by_id("71234", process)

