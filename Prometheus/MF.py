def maze_controller(maze_runner):
	s=0
	while maze_runner.found() == False and s<2000:
		if s%10 == 0:
			cd = 0
		if s%20 == 0:
			cd = 1
		if s%30 == 0:
			cd = 2
		if s%40 == 0:
			cd = 3
		s += 1
		if cd == 1:
			maze_runner.turn_left()
			if maze_runner.go() == False:
				maze_runner.turn_right()
				maze_runner.turn_right()
				if maze_runner.go() == False:
					maze_runner.turn_left()
					if maze_runner.go() == False:
						maze_runner.turn_left()
						maze_runner.turn_left()
			maze_runner.go()
		elif cd == 2:
			maze_runner.turn_right()
			if maze_runner.go() == False:
				maze_runner.turn_left()
				if maze_runner.go() == False:
					maze_runner.turn_left()
					if maze_runner.go() == False:
						maze_runner.turn_left()
		elif cd == 3:
			maze_runner.turn_left()
			if maze_runner.go() == False:
				maze_runner.turn_right()
				if maze_runner.go() == False:
					maze_runner.turn_right()
					if maze_runner.go() == False:
						maze_runner.turn_right()
		else:
			maze_runner.turn_right()
			if maze_runner.go() == False:
				maze_runner.turn_left()
			maze_runner.turn_left()
			if maze_runner.go() == False:
				maze_runner.turn_right()
				if maze_runner.go() == False:
					maze_runner.turn_left()
					if maze_runner.go() == False:
						maze_runner.turn_left()
			maze_runner.go()
