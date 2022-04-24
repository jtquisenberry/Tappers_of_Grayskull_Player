from tappersogp.main import TappersOGPlayer

if __name__ == '__main__':
    svsep = TappersOGPlayer(outfile=r'D:\Projects\tappers.txt')
    ret_val = svsep.start()
    print(str(ret_val))
