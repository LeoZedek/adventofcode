with open('input') as f:
	data = f.readlines()

ORE = 0
CLAY = 1
OBSIDIAN = 2
GEODE = 3

minerals = set()
minerals.add(ORE)
minerals.add(CLAY)
minerals.add(OBSIDIAN)
minerals.add(GEODE)

blueprints = []

for ind, string in enumerate(data):
	blueprint = {}

	string_list = string.split(' ')

	blueprint[ORE] = {
		ORE : int(string_list[6])
	}

	blueprint[CLAY] = {
		ORE : int(string_list[12])
	}

	blueprint[OBSIDIAN] = {
		ORE : int(string_list[18]),
		CLAY : int(string_list[21])
	}

	blueprint[GEODE] = {
		ORE : int(string_list[27]),
		OBSIDIAN : int(string_list[30])
	}

	blueprints.append(blueprint)

def collect_ressource(ressources, robots):

	result = ressources.copy()

	for mineral in result:
		result[mineral] += robots[mineral]

	return result

def max_cost(blueprint_cost, ressource):

	result = 0

	for cost in blueprint_cost.values():
		if ressource in cost:
			result = max(result, cost[ressource])

	return result

def have_enough_ressource_to_build(blueprint_cost, ressources, robot):
	for mineral, cost in blueprint_cost[robot].items():
		if ressources[mineral] < cost:
			return False

	return True

def is_pertinent_to_build(blueprint_cost, robots, robot):
	if robot == GEODE:
		return True

	if robots[robot] < max_cost(blueprint_cost, robot):
		return True

	return False

def build_robot(blueprint_cost, ressources, robot):

	new_ressources = ressources.copy()

	for mineral, cost in blueprint_cost[robot].items():
		new_ressources[mineral] -= cost

	return new_ressources

def max_geode(minutes_remaining, blueprint_cost, ressources, robots, memo):

	if minutes_remaining == 2:
		if have_enough_ressource_to_build(blueprint_cost, ressources, GEODE):
			return 2 * robots[GEODE] + 1
		else:
			return 2 * robots[GEODE]

	key = str(minutes_remaining) + str(blueprint_cost) + str(ressources) + str(robots)

	if key in memo:
		return memo[key]

	geode_max = 0

	for mineral in minerals:
		if have_enough_ressource_to_build(blueprint_cost, ressources, mineral) and is_pertinent_to_build(blueprint_cost, robots, mineral):
			# Build robot
			ressources_temp = build_robot(blueprint_cost, ressources, mineral)

			# Collect ressource
			ressources_temp = collect_ressource(ressources_temp, robots)
			geode_recolt = robots[GEODE]

			# robots is ready
			robots_temp = robots.copy()
			robots_temp[mineral] += 1

			geode_temp = geode_recolt + max_geode(minutes_remaining - 1, blueprint_cost, ressources_temp, robots_temp, memo)
			geode_max = max(geode_max, geode_temp)

	# Collect ressource
	ressources_temp = collect_ressource(ressources, robots)

	geode_temp = robots[GEODE] + max_geode(minutes_remaining - 1, blueprint_cost, ressources_temp, robots, memo)
	geode_max = max(geode_max, geode_temp)

	memo[key] = geode_max

	return geode_max

# Result 1

# result = 0

# for index, blueprint in enumerate(blueprints):
# 	ressources = {
# 		ORE : 0,
# 		CLAY : 0,
# 		OBSIDIAN : 0,
# 		GEODE : 0
# 	}

# 	robots = {
# 		ORE : 1,
# 		CLAY : 0,
# 		OBSIDIAN : 0,
# 		GEODE : 0
# 	}

# 	memo = {}

# 	result += (index + 1) * max_geode(24, blueprint, ressources, robots, memo)

# print(result)

result = 1

for index, blueprint in enumerate(blueprints):
	if index < 3:
		ressources = {
			ORE : 0,
			CLAY : 0,
			OBSIDIAN : 0,
			GEODE : 0
		}

		robots = {
			ORE : 1,
			CLAY : 0,
			OBSIDIAN : 0,
			GEODE : 0
		}

		memo = {}
		result *= max_geode(32, blueprint, ressources, robots, memo)
		print(index)

print(result)