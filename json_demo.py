import json

json_file = open("movie_1.txt", "r", encoding="utf-8")
movie = json.load(json_file)
json_file.close()
print(movie)
print(type(movie))

value = """{
    "title": "Tron: Legacy",
    "composer": "Daft Punk",
    "release_year": "2010",
    "budget": 170000000,
    "actors": null,
    "won_oscar": false
}"""
tron = json.loads(value)
print(tron)
print(type(tron))

string_value = json.dumps(movie, ensure_ascii=False)
print(string_value)

movie2 = {}
movie2["title"] = "Minority Report"
movie2["director"] = "Steven Spielberg"
movie2["composer"] = "John Williams"
movie2["actors"] = ["Tom Cruise", "Colin Farrell", "Samantha Morton",
    "Max von Sydow"]
movie2["is_awesome"] = True
movie2["¨buget"] = 102000000
movie2["cinematographer"] = "Janusz Kami\u0144ski"
print(movie2)
file2 = open("movie_2.txt", "w", encoding="utf-8")
json.dump(movie2, file2, ensure_ascii=False)
file2.close()
