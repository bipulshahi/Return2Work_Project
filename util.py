import json
import pickle
import numpy as np
import pandas as pd

#access datacolumns json file
_dataColumns = ''
_model = ''

rtw_category = ('RTW 13 Weeks','Not RTW 26 Weeks','RTW 26 Weeks')

def read_artifacts():
    global _dataColumns
    global _model
    
    with open('dataColumns.json' , 'r') as f:
        _dataColumns = json.load(f)['columns']

    with open('model.pkl' , 'rb') as f:
        _model = pickle.load(f)


def predict_returnToWorkCategory(claimFinancialYear,agency,ageAtAccident,injuryAgencyGroup,bodilyLocationGroup,mechanismGroup,
                                 natureGroup,major,gender):
  
  input = np.zeros(len(_dataColumns))

  input[0] = claimFinancialYear
  input[1] = agency
  input[2] = ageAtAccident

  input[_dataColumns.index(injuryAgencyGroup)] = 1
  input[_dataColumns.index(bodilyLocationGroup)] = 1
  input[_dataColumns.index(mechanismGroup)] = 1
  input[_dataColumns.index(natureGroup)] = 1
  input[_dataColumns.index(major)] = 1
  input[_dataColumns.index(gender)] = 1

  inp = pd.DataFrame([input])
  inp.columns = _dataColumns

  return rtw_category[_model.predict(inp)[0]]

    
def showColumns():
    return _dataColumns

read_artifacts()
print('Model file Accessed')
#showColumns()
print(predict_returnToWorkCategory(2017,63246,43,'Environmental Agencies',
                                   'Lower Limbs','Body Stressing',
                                   'Sprains, Strains and Dislocations',
                                   'Professionals','Male'))
