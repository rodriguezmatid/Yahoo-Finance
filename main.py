import yfinance as yf
import pandas as pd

# Lista de símbolos de acciones
symbols = ['MELI', 'KO', 'DIS']

# Crear un dataframe vacío para almacenar los datos de las acciones
data = pd.DataFrame()

# Iterar sobre la lista de símbolos de acciones
for symbol in symbols:

    # Obtener los datos de la acción
    stock = yf.Ticker(symbol)

    # Obtener los datos del balance
    balance = stock.financials

    # Obtener los dividendos
    dividends = stock.dividends
    print(dividends[-1])

    # Obtener el cash flow
    cash_flow = stock.cashflow

    # Crear un dataframe con los datos de la acción
    df = pd.DataFrame({
        'symbol': symbol,
        'valor_acciones': stock.fast_info['last_price'],
        'datos_balance': balance.loc['Total Revenue'][0],
        'fecha dividendos': dividends.index[-2],
        'dividendos': dividends[-1],
        'cash_flow': cash_flow.loc['Operating Cash Flow'][0]
    }, index=[0])

    # Agregar los datos al dataframe
    data = data.append(df, ignore_index=True)

# Guardar los datos en un archivo CSV
data.to_csv("acciones.csv", index=False)