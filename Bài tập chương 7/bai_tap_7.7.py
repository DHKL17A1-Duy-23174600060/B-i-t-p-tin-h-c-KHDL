def doi_tien(so_tien):
    so_to_500000 = so_tien // 500000
    so_tien = so_tien % 500000

    so_to_200000 = so_tien // 200000
    so_tien = so_tien % 200000

    so_to_100000 = so_tien // 100000
    so_tien = so_tien % 100000

    so_to_50000 = so_tien // 50000
    so_tien = so_tien % 50000

    print("Số tờ 500,000:", so_to_500000)
    print("Số tờ 200,000:", so_to_200000)
    print("Số tờ 100,000:", so_to_100000)
    print("Số tờ 50,000:", so_to_50000)
    print("Tiền còn lại:", so_tien)

so_tien_muon_doi = int(input("Số tiền muốn đổi: "))
doi_tien(so_tien_muon_doi)

