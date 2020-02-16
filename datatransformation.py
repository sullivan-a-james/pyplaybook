
#Data Transposition Function: 

def transpose(dataframe,values,keys=None):
    
    """
    The transpose function allows you to 'flip' the orientation of a pandas dataframe whereby 
    one or many horizontal data columns can be viewed on a vertical axis
    
    Parameters
    ----------
    dataframe : pandas dataframe
        Select a pandas dataframe to undergo transposition.
    values : string or list
        Select the column name or list of column names which will be pivoted so as that
        their horizontally stored data is re-positioned on a vertical axis.
    keys : string or list
        Select the column name or list of column names to pivot the dataframe around. 
        The name of these column(s) will remain on the horizontal axis, 
        with values replicated vertically for each column selected as values.

    Returns
    -------
    DataFrame
        The number of rows your dataframe will end up with after transposing equates to 
        the number of initial rows times-by the number of values columns selected.
    
    """
    import pandas as pd
    
    null_index_name = 0
    
    if dataframe.index.name is None:
        null_index_name += 1
        i = 0
        dataframe.index.name = str(i)
        while dataframe.index.name in list(dataframe.columns.values):
            i += 1
            dataframe.index.name = str(i)
    
    if type(values) != list:
        values = [values]
        
    if keys is None:
        keys = []
    elif type(keys) != list:
        keys = [keys]
    
    AttributeName = "AttributeName"
    AttributeValue = "AttributeValue"

    if AttributeName in list(dataframe.columns.values):
        i = 1
        while AttributeName in list(dataframe.columns.values):
            i += 1
            AttributeName = "AttributeName_"+str(i)

    if AttributeValue in list(dataframe.columns.values):
        i = 1
        while AttributeValue in list(dataframe.columns.values):
            i += 1
            AttributeValue = "AttributeName_"+str(i)


    dfi = dataframe.reset_index()
    dfi.index = range(1,len(dataframe)+1)

    tdf = pd.DataFrame(dfi[values].stack(dropna=False)).rename(columns={0:AttributeValue})
    tdf.reset_index(inplace=True)
    tdf.rename(columns={list(tdf.columns.values)[1]:AttributeName},inplace=True)
    tdf.index = tdf[list(tdf.columns.values)[0]]
    tdf.drop(list(tdf.columns.values)[0],axis=1,inplace=True)

    df_output = dfi.join(tdf)
    df_output.index = df_output[dataframe.index.name]
    df_output.drop(dataframe.index.name,axis=1,inplace=True)
    keys.append(AttributeName)
    keys.append(AttributeValue)
    df_output = df_output[keys]
    if null_index_name == 1:
        df_output.index.name = None
        dataframe.index.name = None
    return df_output
