import pandas as pd
from pathlib import Path

# locate xlsx
downloads_path = str(Path.home() / "Downloads")
ALMAdf = pd.read_excel(downloads_path + "/Alma.xlsx")  # contains 001 (MMS), 035$a (OCLC#) from Alma records
OCLCdf = pd.read_excel(downloads_path + "/OCLC.xlsx")  # contains 001 (OCLC#) from worldshare collection

# get OCLC from each xlsx
ALMAdf['035$a'] = ALMAdf['035$a'].str.findall(r'\(OCoLC\)ocm\d{8}|\(OCoLC\)ocn\d{9}|\(OCoLC\)on\d{10}')
ALMAdf['035$a'] = ALMAdf['035$a'].astype(str)
ALMAdf['035$a'] = ALMAdf['035$a'].str.findall(r'ocm\d{8}|ocn\d{9}|on\d{10}')
OCLCdf['001'] = OCLCdf['001'].str.findall(r'ocm\d{8}|ocn\d{9}|on\d{10}')
ALMAdf['035$a'] = ALMAdf['035$a'].str[0]
OCLCdf['001'] = OCLCdf['001'].str[0]

# find unmatched
NotInOCLC = ALMAdf[~ALMAdf['035$a'].isin(OCLCdf['001'])]
NotInAlma = OCLCdf[~OCLCdf['001'].isin(ALMAdf['035$a'])]
NotInOCLC.to_csv(downloads_path + "/NotInOCLC.csv", index=False)
NotInAlma.to_csv(downloads_path + "/NotInAlma.csv", index=False)
