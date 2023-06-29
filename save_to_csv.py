import menu_parse
import csv

res_list = []
symb_to_clear = '''"",.'' \n'''

# Remove unwanted symbols
for i in menu_parse.get_menu():
    # Only dishes are picked
    if i['type'] == 'dish':
        if i['price']['value']:
            if i['description']:
                res_list.append([i['restaurant'].strip(symb_to_clear), i['name']['value'].strip(symb_to_clear).replace('\n', ' '), i['price']['value'], i['description']['value'].strip(symb_to_clear).replace('\n', ' ')])
            else:
                res_list.append([i['restaurant'].strip(symb_to_clear), i['name']['value'].strip(symb_to_clear).replace('\n', ' '), i['price']['value'], '-'])
# Save result to CSV file
with open('../output.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(res_list)