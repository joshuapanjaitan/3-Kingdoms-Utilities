import numpy as np

window = True
char = []
points = []
print("""
    Pilih Jenis Expedition
    1. JiYin
    2. Daxing
    3. HuiJi
""")
exp = input("Masukkan Nomor Expedisi : ")
varChar = input("Masukkan jumlah Character : ")
for i in range(int(varChar)):
    nick = input('Masukkan IGN ke {} :'.format(i+1))
    char.append(nick)
    points.append(0)

expPoints = np.array(points)


while (window):
    try:
        curr = input("Masukkan Point : ")
        cp = curr.split(" ")
        cp = [int(i) for i in cp]
        curr_points = np.array(cp)
        curr_points = curr_points * int(exp)
        expPoints = curr_points + expPoints
        for a in range(int(varChar)):
            ign = char[a]
            pw = expPoints[a]
            print("{} : {}".format(ign, pw))
    except:
        print("Pastikan Input Sudah Benar")
