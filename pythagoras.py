import pygame, math

def get_target(pos, angle, distance):
	alpha = angle
	c = distance
	a = c * math.sin(math.radians(alpha))

	if angle == 0:
		return (pos[0], pos[1] - distance)
	elif angle == 90:
		return (pos[0] - distance, pos[1])
	elif angle == 180:
		return (pos[0], pos[1] + distance)
	elif angle == 270:
		return (pos[0] + distance, pos[1])
	elif angle > 0 and angle < 90:
		beta = 90-alpha
		b = math.sqrt(-a**2+c**2)
		#print("a",a,"b",b,"c",c,"alpha",alpha,"beta",beta)
		return (pos[0] - a, pos[1] - b)
	elif angle > 90 and angle < 180:
		beta = 180-alpha
		b = math.sqrt(-a**2+c**2)
		#print("a",a,"b",b,"c",c,"alpha",alpha,"beta",beta)
		return (pos[0] - a, pos[1] + b)
	elif angle > 180 and angle < 270:
		beta = 270-alpha
		b = math.sqrt(-a**2+c**2)
		#print("a",a,"b",b,"c",c,"alpha",alpha,"beta",beta)
		return (pos[0] - a, pos[1] + b)
	elif angle > 270 and angle < 360:
		beta = 360-alpha
		b = math.sqrt(-a**2+c**2)
		#print("a",a,"b",b,"c",c,"alpha",alpha,"beta",beta)
		return (pos[0] - a, pos[1] - b)




	pass