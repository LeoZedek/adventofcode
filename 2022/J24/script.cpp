#include<iostream>
#include<string>
#include<fstream>
#include<vector>
#include<queue>
#include<set>
#include<unordered_set>
#include<tuple>
#include<unordered_map>
#include<cstdlib>
#include<time.h>

using namespace std;

struct hash_tuple {
  
    template <class T1, class T2>
  
    size_t operator()(
        const tuple<T1, T2>& x)
        const
    {
        return get<0>(x) * 1000 + get<1>(x);
    }
};

struct hash_tuple2 {
  
    template <class T1, class T2>
  
    size_t operator()(
        const tuple<T1, T2>& x)
        const
    {
        return get<0>(get<0>(x)) * 1000 + get<1>(get<0>(x)) + get<1>(x) * 1000000;
    }
};

typedef tuple<int, int> coordonnee;
typedef unordered_map<coordonnee, unordered_set<char>, hash_tuple> my_type_map;

void add_to_map(my_type_map* my_map, int i, int j, char wind) {
	coordonnee position = tuple(i, j);

	if ((*my_map).find(tuple(i, j)) != (*my_map).end()) {
		(*my_map).at(position).insert(wind);
	}
	else {
		unordered_set<char> set_temp;
		set_temp.insert(wind);

		(*my_map).insert(pair<coordonnee, unordered_set<char>> (position, set_temp));
	}
}

my_type_map update(my_type_map* my_map, int height, int width) {
	my_type_map result;

	my_type_map::iterator it;

	for (it = (*my_map).begin(); it != (*my_map).end(); it++) {
		int i, j;

		coordonnee coord = it->first;
		unordered_set<char> winds = it->second;

		i = get<0>(coord);
		j = get<1>(coord);

		unordered_set<char>::iterator it_winds;

		for (it_winds = winds.begin(); it_winds != winds.end(); it_winds++) {
			char wind = *it_winds;

			if (wind == '^') {
				if (i - 1 >= 1) {
					add_to_map(&result, i - 1, j, wind);
				}
				else {
					add_to_map(&result, height - 2, j, wind);
				}
			}

			else if (wind == 'v') {
				if (i + 1 < height - 1) {
					add_to_map(&result, i + 1, j, wind);
				}
				else {
					add_to_map(&result, 1, j, wind);
				}
			}

			else if (wind == '<') {
				if (j - 1 >= 1) {
					add_to_map(&result, i, j - 1, wind);
				}
				else {
					add_to_map(&result, i, width - 2, wind);
				}
			}
			else if (wind == '>') {
				if (j + 1 < width - 1) {
					add_to_map(&result, i, j + 1, wind);
				}
				else {
					add_to_map(&result, i, 1, wind);
				}
			}
		}
	}

	return result;
}

int distance_manhatan(coordonnee* pos1, coordonnee* pos2) {
	return abs(get<0>(*pos1) - get<0>(*pos2)) + abs(get<1>(*pos1) - get<1>(*pos2));
}

bool is_valide(my_type_map* my_map, coordonnee* position, int height, int width) {
	if (*position == tuple(0, 1) or *position == tuple(height - 1, width - 2)) {
		return true;
	}
	else {
		int row, column;
		row = get<0>(*position);
		column = get<1>(*position);
		return !(row == 0 or row == height - 1 or column == 0 or column == width - 1 or ((*my_map).find(*position) != (*my_map).end()));
	}
}

set<coordonnee> voisins(unordered_map<int, my_type_map>* configurations_map, coordonnee* position, int index, int seuil, int height, int width) {
	int new_index;

	if (index == seuil - 1) {
		new_index = 0;
	}
	else {
		new_index = index + 1;
	}

	int row, column;
	row = get<0>(*position);
	column = get<1>(*position);

	set<coordonnee> voisins_possible;
	voisins_possible.insert(tuple(row, column));
	voisins_possible.insert(tuple(row + 1, column));
	voisins_possible.insert(tuple(row - 1, column));
	voisins_possible.insert(tuple(row, column + 1));
	voisins_possible.insert(tuple(row, column - 1));

	set<coordonnee> result;
	set<coordonnee>::iterator it;

	for (it = voisins_possible.begin(); it != voisins_possible.end(); it++) {
		coordonnee voisin = *it;

		if (is_valide(&(*configurations_map).at(new_index), &voisin, height, width)) {
			result.insert(voisin);
		}
	}

	return result;
}

tuple<int, int> get_shorter_ways_BFR(unordered_map<int, my_type_map>* configurations_map, coordonnee* begin, coordonnee* end, int index_begin, int seuil, int height, int width) {
	unordered_map<tuple<coordonnee, int>, int, hash_tuple2> distance;
	unordered_set<tuple<coordonnee, int>, hash_tuple2> configuration_marque;

	queue<tuple<coordonnee, int>> my_queue;
	my_queue.push(tuple(*begin, index_begin));

	distance.insert(pair<tuple<coordonnee, int>, int> (tuple(*begin, index_begin), 0));
	configuration_marque.insert(tuple(*begin, index_begin));

	while (!my_queue.empty()) {
		coordonnee position = get<0>(my_queue.front());
		int index = get<1>(my_queue.front());

		my_queue.pop();

		int new_index;

		if (index == seuil - 1) {
			new_index = 0;
		}
		else {
			new_index = index + 1;
		}

		set<coordonnee> voisins_set = voisins(configurations_map, &position, index, seuil, height, width);
		set<coordonnee>::iterator it;

		for (it = voisins_set.begin(); it != voisins_set.end(); it++) {
			coordonnee voisin = *it;

			if (configuration_marque.find(tuple(voisin, new_index)) == configuration_marque.end()) {

				distance.insert(pair<tuple<coordonnee, int>, int> (tuple(voisin, new_index), distance.at(tuple(position, index)) + 1));
				my_queue.push(tuple(voisin, new_index));

				configuration_marque.insert(tuple(voisin, new_index));
				
				if (voisin == *end) {

					return tuple(distance.at(tuple(*end, new_index)), index);
				}
			}
		}
	}
}

int main(int argc, char* argv[]) {
	time_t time1, time2;
	time(&time1);

	ifstream my_file;
	string my_string;
	vector<string> data;

	if (argc < 2) {
		cout << "Non de fichier non spécifier. Fichier choisie par defaut : input\n";
		my_file.open("input");
	}
	else {
		my_file.open(argv[1]);
	}

	while (!my_file.eof()) {
		getline(my_file, my_string);
		if (my_string != "") {
			data.push_back(my_string);
		}
	}

	unordered_set<char> winds;
	winds.insert('v');
	winds.insert('<');
	winds.insert('>');
	winds.insert('^');
	
	int height, width;

	height = data.size();
	width = data.at(0).size();
	coordonnee begin_position, exit_position;

	begin_position = tuple(0, 1);
	exit_position = tuple(height - 1, width - 2);

	my_type_map my_map;

	for (int i = 0; i < height; i++) {
		for (int j = 0; j < width; j++) {

			char letter = data.at(i).at(j);

			if (winds.find(letter) != winds.end()) {

				if (my_map.find(tuple(i, j)) == my_map.end()) {
					unordered_set<char> set_temp;
					set_temp.insert(letter);

					my_map.insert(pair<coordonnee, unordered_set<char>> (tuple(i, j), set_temp));
				}
				else {
					my_map.at(tuple(i, j)).insert(letter);
				}
			}
		}
	}

	unordered_map<int, my_type_map> configurations_map;

	configurations_map.insert(pair<int, my_type_map>(0, my_map));

	int seuil = (height - 2) * (width - 2);

	my_type_map temp_map = my_map;

	for (int i = 1; i < seuil; i++) {
		temp_map = update(&temp_map, height, width);
		configurations_map.insert(pair<int, my_type_map>(i, temp_map));
	}

	cout << "Config unordered_maps finished\n";

	int result = 0;
	int minutes, index;
	
	coordonnee tuple_result = get_shorter_ways_BFR(&configurations_map, &begin_position, &exit_position, 0, seuil, height, width);

	minutes = get<0>(tuple_result);
	index = get<1>(tuple_result);

	cout << minutes << '\n';

	result += minutes;

	tuple_result = get_shorter_ways_BFR(&configurations_map, &exit_position, &begin_position, index, seuil, height, width);

	minutes = get<0>(tuple_result);
	index = get<1>(tuple_result);

	cout << minutes << '\n';
	result += minutes;

	tuple_result = get_shorter_ways_BFR(&configurations_map, &begin_position, &exit_position, index, seuil, height, width);

	minutes = get<0>(tuple_result);
	index = get<1>(tuple_result);

	cout << minutes << '\n';
	result += minutes;

	cout << result - 2 << '\n';

	time(&time2);

	cout << "temps : " << time2 - time1 << '\n';
}
