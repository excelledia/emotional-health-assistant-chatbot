import json
import pandas as pd
import xlsxwriter

from helper import get_response 

data_file = open('tests.json', 'r', encoding='utf8').read()
intents = json.loads(data_file)

def chatbot_response_test():
	
	counter = 0
	success = 0

	true_queries = []
	true_response = []
	false_queries = []
	false_response = []
	
	for intent in intents['intents']:
		for pattern in intent['patterns']:
			counter += 1
			response = str(get_response(pattern,1))
			if response in intent['responses']:
				true_queries.append(pattern)
				true_response.append(response)
				success += 1
			else:
				false_queries.append(pattern)
				false_response.append(response)

	
	writer = pd.ExcelWriter('test_report.xlsx', engine='xlsxwriter')
	df_true = pd.DataFrame({'Query': true_queries, 'Response':true_response})
	df_false = pd.DataFrame({'Query': false_queries, 'Response':false_response})
	
	df_true.to_excel(writer, sheet_name='True Response')
	df_false.to_excel(writer, sheet_name='False Response')

	writer.save()			
	print('Accuracy: '+str(success/counter*100)+'%')

chatbot_response_test()