import xlsxwriter
import subprocess
from get_expenses import get_expenses

print('Starting script...')

print('Grabbing data from xlsx file...')
input_path = 'input/fatura.xlsx'
keywords_to_filter = ['Pagamento em', 'Conversão', 'IOF']
keywords_to_combine = ['Ifood', 'Uber', 'Rappi',
                       'Discord', 'Microsoft', 'Azul', 'Decolar', 'Steam']

expenses = get_expenses(input_path,
                        keywords_to_filter, keywords_to_combine)


print('Generating final xlsx file...')
output_path = 'output/calculo_fatura.xlsx'

workbook = xlsxwriter.Workbook(output_path)
worksheet = workbook.add_worksheet()

expenses.insert(0, ['Compra', 'Valor'])
expenses.append(['Total', f'=SUM(B1:B{len(expenses)})'])

row = 0

for item, cost in expenses:
    worksheet.write(row, 0, item)
    worksheet.write(row, 1, cost)
    row += 1

workbook.close()

print('Done!')
print(f'Check {output_path}!')
subprocess.run(['start', '', output_path], shell=True)
