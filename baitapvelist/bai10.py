# Nhập một câu, tách thành List các từ, tìm từ dài nhất
cau= input("Nhap mot cau:")
tu_list= cau.split()
do_dai_lon_nhat= max(len(tu) for tu in tu_list)
tu_dai_nhat = [tu for tu in tu_list if len(tu) == do_dai_lon_nhat]
print("Danh sach tu:", tu_list)
print("Do dai tu dai nhat:", do_dai_lon_nhat)
print("Tu dai nhat", tu_dai_nhat)