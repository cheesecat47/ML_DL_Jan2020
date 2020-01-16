def set_font():
    import platform
    import matplotlib.font_manager as fm

    system_name = platform.system()
    if system_name == 'Windows':
        return 'Malgun Gothic'
    elif system_name == 'Darwin':
        return 'AppleGothic'
    elif system_name == 'Linux':
        path = '/usr/share/font/truetype/nanum/NanumMyeongjo.ttf'
        font_name = fm.FontProperties(fname=path, size=12)
        return font_name


if __name__ == "__main__":
    set_font()
    # usage: plc.rt('font', family=set_font())
    # to present minus sign: plt.rcParams['axes.unicode_minus'] = False

