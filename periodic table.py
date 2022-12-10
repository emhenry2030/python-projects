"""Periodic Table of Elements, by Emily Henry
Displays atomic information for all elements.
Veiw this code at https://nostarch.com/big book small python projects
Tag: short, science"""

# Data from https://en.wikipedia.org/wiki/List_of_chemical_elements
# Highlight the table, copy it, then paste it into a spreadsheet program
# like Excel or Google Sheets like in https://invpy.com/elements
# Then save this file as periodictable.csv.
# Or download this csv file from https://invpy.com/periodictable.csv.

import csv, sys, re

# Read in all data from periodictable.csv.
elementsFile = open('periodictable.csv.', encoding='utf-8')
elementsCsvReader = csv.reader(elementsFile)
elements = list(elementsCsvReader)
elementsFile.close()

ALL_COLUMNS = ['Atomic Number', 'Symbol', 'Elements', 'Origin of name',
               'Group', 'Period', 'Atomic weight', 'Density',
               'Melting point', 'Boiling point',
               'Specific heat capcity', 'Electronegativity',
               'Abundance in earth\'s crust']

# To justify the text, we need to find the logest string in ALL_COLUMNS.
LONGEST_COLMN = 0
for key in ALL_COLUMNS:
    if len(key) > LONGEST_COLUMN:
        LONGEST_COLUMN = len(key)
        
# Put all the elements data into a data structure:
ELEMENTS = {} # The data structure that stores all element data.
for line in elements:
    element = { 'Atomic Number':  line[0],
                'Symbol':         line[1],
                'Element':        line[2],
                'Origin of name': line[3],
                'Group':          line[4],
                'Period':         line[5],
                'Atomic weight':  line[6] + ' u', # atomic mass unit
                'Density':        line[7] + ' g/cm^3' , # grams/cubic cm
                'Melting point':  line[8] + ' k', # kelvin
                'Boiling point':  line[9] + ' k', # kelvin
                'Specific heat capacity':      line[10] + ' J/(g*K)',
                'Electronegativity':           line[11],
                'Abundance in earth\'s crust': line[12] + ' mg/kg'}
                