from pathlib import Path
import json
from dataclasses import asdict, replace

from shapes import Shape, Circle, Rectangle, Triangle

FILE_NAME = 'list.json'
FILE_PATH = Path(FILE_NAME)

def add_shape(shape: Shape) -> None:

	if not FILE_PATH.exists():
		with open(FILE_NAME, 'w') as file:
			json.dump([], file, indent=4)

	with open(FILE_NAME, 'r+') as file:
		data = json.load(file)
		data.append(asdict(shape))
		file.seek(0)
		json.dump(data, file, indent=4)

def get_shapes() -> list[Shape]:
	with open(FILE_NAME, 'r') as file:
		data = json.load(file)
	shapes = []
	for shape in data:
		if shape['name'] == 'circle':
			shapes.append(Circle(**shape))
		elif shape['name'] == 'rectangle':
			shapes.append(Rectangle(**shape))
		elif shape['name'] == 'triangle':
			shapes.append(Triangle(**shape))	
	return shapes

def remove_shape(shape: Shape) -> None:
	with open(FILE_NAME, 'r+') as file:
		data = json.load(file)
		for index, shape_dict in enumerate(data):
			if shape_dict['name'] == shape.name:
				data.pop(index)
				break
		file.seek(0)
		json.dump(data, file, indent=4)

def clear_shapes() -> None:
	with open(FILE_NAME, 'w') as file:
		json.dump([], file, indent=4)
