import pandas as pd

'''
Reading Data:
You can use the read functions to read from a variety of files
csv: use read_csv
sas: use read_sas
Special note: In case you want to read sas7bdat files, it is recommended to use the pyreadstat library:
https://github.com/Roche/pyreadstat

parquet: use pyarrow.parquet
'''

#reading df from a csv
df = pd.read_csv('C://Work/Python/279df7e5-e540-4e2f-9b4b-dc655e8007e1_Data.csv')
#read sas:
df_sas = pd.read_sas('path/to/sas/my_sas.sas7bdat')
# with the new library for SAS7bdat:
import pyreadstat
df_sas,meta = pyreadstat.read_sas7bdat('path/to/sas/my_sas.sas7bdat')

# parquet:
import pyarrow.parquet as pq
df_parquet = pq.read_table('path/to/pq/my_parquet')
df = df_parquet.to_pandas()
# optional - delete pq in RAM to save space:
del df_parquet


