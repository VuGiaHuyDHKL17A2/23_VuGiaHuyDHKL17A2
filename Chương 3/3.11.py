import numpy as np

# Đọc dữ liệu từ file stocks1.csv, stocks2.csv, companies.csv
stocks1 = np.genfromtxt('stocks1.csv', delimiter=',', dtype=None, names=True, encoding='utf-8')
stocks2 = np.genfromtxt('stocks2.csv', delimiter=',', dtype=None, names=True, encoding='utf-8')
companies = np.genfromtxt('companies.csv', delimiter=',', dtype=None, names=True, encoding='utf-8')

# a) stocks1
print("Dữ liệu đầu của stocks1:", stocks1[:5])
print("Dữ liệu cuối của stocks1:", stocks1[-5:])

# b) stocks2
print("Dữ liệu đầu của stocks2:", stocks2[:5])
print("Dữ liệu cuối của stocks2:", stocks2[-5:])

# c) companies
print("Dữ liệu đầu của companies:", companies[:5])
print("Dữ liệu cuối của companies:", companies[-5:])

# 2. Check Null và thay thế với max hoặc min
isnull_stocks1 = np.isnan(stocks1['close'])
stocks1['close'][isnull_stocks1] = np.max(stocks1['close'])

isnull_stocks2 = np.isnan(stocks2['close'])
stocks2['close'][isnull_stocks2] = np.min(stocks2['close'])

# 3. Tạo dataframe stocks bằng cách ghép stocks1 và stocks2 theo dòng
stocks = np.concatenate((stocks1, stocks2))
print("Dữ liệu cuối cùng của stocks:", stocks[-15:])

# 4. Tạo dataframe stocks_companies bằng cách ghép stocks với companies
companies_dict = {row['symbol']: row for row in companies}
stocks_companies = np.array([np.append(row, companies_dict.get(row['symbol'], np.full(len(companies[0]), np.nan))) for row in stocks])
print("Dữ liệu cuối cùng của stocks_companies:", stocks_companies[-5:])

# 5. Biết giá đóng cửa trung bình
mean_close = np.mean(stocks_companies[:, stocks.dtype.names.index('close')])
print("Giá đóng cửa trung bình:", mean_close)

# 6. Biết giá đóng cửa lớn nhất và nhỏ nhất
max_close = np.max(stocks_companies[:, stocks.dtype.names.index('close')])
min_close = np.min(stocks_companies[:, stocks.dtype.names.index('close')])
print("Giá đóng cửa lớn nhất:", max_close)
print("Giá đóng cửa nhỏ nhất:", min_close)

# 7. Tạo cột parsed_time và đổi thời gian sang dạng DateTime
parsed_time = np.array([np.datetime64(row['date'], 'D') for row in stocks_companies])
stocks_companies = np.append(stocks_companies, parsed_time[:, None], axis=1)

# 8. Thêm cột result cho biết close > open
result = np.where(stocks_companies[:, stocks.dtype.names.index('close')] > stocks_companies[:, stocks.dtype.names.index('open')], 'up', 'down')
stocks_companies = np.append(stocks_companies, result[:, None], axis=1)