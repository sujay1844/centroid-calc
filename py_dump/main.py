from shapes import Shape, Circle, Rectangle, Triangle
from fs_helper import add_shape, get_shapes, remove_shape, clear_shapes

def compute_centroid(shapes: list[Shape]) -> tuple[float, float]:
	x = 0
	y = 0
	total_area = 0
	for shape in shapes:
		x += shape.x * shape.area
		y += shape.y * shape.area
		total_area += shape.area
	return x / total_area, y / total_area

def main():
	choice = 0
	while choice != 9:
		print('\n\n\n')
		print('1. Add a shape')
		print('2. Remove a shape')
		print('3. Clear all shapes')
		print('4. Print all current shapes')
		print('5. Compute centroid')
		print('9. Exit')
		choice = int(input('Enter your choice: '))
		print('\n\n\n')
		if choice == 1:
			print('1. Circle')
			print('2. Rectangle')
			print('3. Triangle')
			choice = int(input('Enter your choice: '))
			if choice == 1:
				x = float(input('Enter x: '))
				y = float(input('Enter y: '))
				radius = float(input('Enter radius: '))
				is_filled = False if input('Is it filled? (Y/n): ') == 'n' else True

				circle = Circle(x=x, y=y, radius=radius, is_filled=is_filled)
				add_shape(circle)

			elif choice == 2:
				x = float(input('Enter x: '))
				y = float(input('Enter y: '))
				width = float(input('Enter width: '))
				height = float(input('Enter height: '))
				is_filled = False if input('Is it filled? (Y/n): ') == 'n' else True

				rectangle = Rectangle(x=x, y=y, width=width, height=height, is_filled=is_filled)
				add_shape(rectangle)
			elif choice == 3:
				x = float(input('Enter x: '))
				y = float(input('Enter y: '))
				base = float(input('Enter base: '))
				height = float(input('Enter height: '))
				is_filled = False if input('Is it filled? (Y/n): ') == 'n' else True

				triangle = Triangle(x=x, y=y, base=base, height=height, is_filled=is_filled)
				add_shape(triangle)
			else:
				print('Invalid choice')
		elif choice == 2:
			print('Enter data of the shape to be removed')
			print('1. Circle')
			print('2. Rectangle')
			print('3. Triangle')
			del_choice = int(input('Enter your choice: '))
			if del_choice == 1:
				x = float(input('Enter x: '))
				y = float(input('Enter y: '))
				radius = float(input('Enter radius: '))

				circle = Circle(x, y, radius)
				remove_shape(circle)
			elif del_choice == 2:
				x = float(input('Enter x: '))
				y = float(input('Enter y: '))
				width = float(input('Enter width: '))
				height = float(input('Enter height: '))

				rectangle = Rectangle(x, y, width, height)
				remove_shape(rectangle)
			elif del_choice == 3:
				x = float(input('Enter x: '))
				y = float(input('Enter y: '))
				base = float(input('Enter base: '))
				height = float(input('Enter height: '))

				triangle = Triangle(x, y, base, height)
				remove_shape(triangle)
		elif choice == 3:
			confirmation = input('Are you sure you want to clear all shapes? (y/n): ')
			if confirmation == 'y':
				clear_shapes()
			elif confirmation == 'n':
				pass
			else:
				print('Invalid input')
		elif choice == 4:
			shapes = get_shapes()
			if shapes:
				print("Current shapes:-")
				for shape in shapes:
					print(shape)
		elif choice == 5:
			centroid = compute_centroid(get_shapes())
			print(f'Centroid: {centroid}')
		elif choice == 9:
			pass
		else:
			print('Invalid choice')

if __name__ == '__main__':
	main()