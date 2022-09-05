import pandas as pd

from mancalog.scripts.numba_wrapper.numba_types.node_type import Node


class Filter:

    def filter_by_bound(self, dataframe, label, bound, display_other_labels=False):
        # dataframe is a list of dictionaries mapping labels to bounds
        if display_other_labels:    
            columns = ['component', label, 'other labels']
        else:
             columns = ['component', label]
        df = pd.DataFrame(columns=columns)
        d = {}
        for row in dataframe:
            if row['component'] == Node('n2825'):
                print(row['success'], row['success'] in bound)
            if label in row.keys() and row[label] in bound:
                d['component'] = row['component']
                d[label] = row[label]
                if display_other_labels:
                    d['other labels'] = {x:row[x] for x in row.keys() if (x!='component' and x!=label)}
                df.loc[len(df.index)] = d
        return df        