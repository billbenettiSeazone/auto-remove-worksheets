# imports
from openpyxl import load_workbook
import argparse
import sys

# set file path
filepath="./planilha_01.xlsx"

#get the file
args = sys.argv[0]

def run(file):    
    # load demo.xlsx 
    try:
        wb=load_workbook(filepath)
        try:
            # if spreadsheet is opened then try to remove
            wb.remove(wb.get_sheet_by_name('Datas Livres'))
            wb.remove(wb.get_sheet_by_name('TO'))
            # save workbook
            wb.save(filepath)
            # if spreadsheet is opened and we don't have the selected sheets, then close
        except:
            print("O arquivo selecionado não possui as tabs para remoção")
    except:
        print("Não foi possível alterar a planilha!\nVerifique a o nome do arquivo!")

        
run(args)
