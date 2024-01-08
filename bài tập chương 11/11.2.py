# 11.2

teams=[
    ['steven','neena','lex','alexander','bruce'],
    ['david','jack5cu','bill','tom','mike','daniel'],
    ['alexander','adam','kevin','sigal','mike']
]
def chon_doi_truong(teams):
    doi_te_nhat=teams[-1]
    doi_truong=doi_te_nhat[1]
    return doi_te_nhat

doi_truong_te_nhat=chon_doi_truong(teams)
print("Đội trưởng của đội tệ nhất là:",doi_truong_te_nhat)