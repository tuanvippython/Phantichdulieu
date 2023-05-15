import pandas as pd

# Đọc dữ liệu
data = pd.read_excel("C:/Users/ADMIN/Downloads/Book1_Temperature.xlsx")

# Lấy cột dữ liệu của data bằng cách gọi tên cột
lay_cot = data["Temperature"]
print(lay_cot)

# Hiển thị ra các giá trị chứa giá trị NA ra màn hình (hiển thị là True)
missing_values = data.isna()

# Tính tổng của cột nhiệt độ và bỏ qua các hàng có chứa giá trị NA
sum_value = data["Temperature"].sum(skipna=True)
print(sum_value)

# TÍnh giá trị trung bình của cột nhiệt độ bằng cách lấy tổng chia cho số lượng của cột nhiệt độ
mean_value = (sum_value) / len(data["Temperature"])
print("Giá trị trung bình của nhiệt độ là: ",mean_value)

# Giá trị lớn nhất của độ mặn theo năm
max_value_sanility = data.groupby("Year")["Salinity"].max()
print("Giá trị lớn nhất của độ mặn theo năm là: ", max_value_sanility)

# Giá trị lớn nhất của nhiệt độ theo năm
max_value_Temperature = data.groupby("Year")["Temperature"].max()
print("Giá trị lớn nhất của nhiệt độ theo năm là: ",max_value_Temperature)

# Giá trị lớn nhất của CHLFa theo năm
max_value_CHLFa = data.groupby("Year")["CHLFa"].max()
print("Giá trị lớn nhất của CHLFa theo năm là: ",max_value_CHLFa)

# Giá trị nhỏ nhất của độ mặn theo năm
min_value_salinity = data.groupby("Year")["Salinity"].min()
print("Giá trị nhỏ nhất của độ mặn theo năm là: ", min_value_salinity)

# Giá trị nhỏ nhất của nhiệt độ theo năm
min_value_Temperature = data.groupby("Year")["Temperature"].min()
print("Giá trị nhỏ nhất của nhiệt độ theo năm là: ",min_value_Temperature)

# Giá trị nhỏ nhất của CHLFa theo năm
min_value_CHLFa = data.groupby("Year")["CHLFa"].min()
print("Giá trị nhỏ nhất của CHLFa theo năm là: ",min_value_CHLFa)



