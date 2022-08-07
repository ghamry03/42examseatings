from api.intra import ic

file = input("file: ")

url = input("http://api.intra.42.fr/v2/")
ic.progress_bar = True
response = ic.pages_threaded(f"https://api.intra.42.fr/v2/{url}")


with open(f"{file}", "w") as fd:
	for data in response:
		fd.write(f"{data}\n")
