gio_tieu_chuan = 44

so_gio_lam = int(input("Nhập số giờ làm việc: "))
luong_mot_gio = int(input("Nhập lương một giờ: "))

gio_lam_khong_tang_ca = min(so_gio_lam, gio_tieu_chuan)
gio_lam_tang_ca = max(0, so_gio_lam - gio_tieu_chuan)
luong = gio_lam_khong_tang_ca * luong_mot_gio + gio_lam_tang_ca * luong_mot_gio * 1.5
print("Lương tháng này là: " + str(luong))