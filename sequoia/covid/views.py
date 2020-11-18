from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import csv
import json


def index(request):
	state = request.GET['state']
	print(state)
	state_data = []
	with open("./covid_data.csv", "r") as f:
		reader = csv.reader(f, delimiter="\t")
		for i, line in enumerate(reader):
			if i == 0:
				header = line[0].split(",")
				index = header.index("Province_State")
			else:
				data = line[0].split(",")
				if data[index].lower() == state.lower():
					data[10] = data[10]+data[11]+data[12]
					data.pop(11)
					data.pop(11)
					state_data.append(dict(zip(header, data)))

	return JsonResponse({'data': state_data})
