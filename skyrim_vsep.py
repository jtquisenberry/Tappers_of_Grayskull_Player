from tappersogp.main import SkyrimVSEPlayer

if __name__ == '__main__':
    svsep = SkyrimVSEPlayer(outfile=r'D:\Projects\tappers.txt')
    ret_val = svsep.start()
    print(str(ret_val))
