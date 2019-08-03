# 필요한 패키지와 라이브러리를 가져옴 
# http://corazzon.github.io/matplotlib_font_setting

# 필요한 패키지와 라이브러리를 가져옴
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 그래프에서 마이너스 폰트 깨지는 문제에 대한 대처
mpl.rcParams['axes.unicode_minus'] = False

import numpy as np

font_name = fm.FontProperties(fname='c:/Windows/Fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)


data = np.random.randint(-100, 100, 50).cumsum()
data

plt.plot(range(50), data, 'r')
mpl.rcParams['axes.unicode_minus'] = False
plt.title('시간별 가격 추이')
plt.ylabel('English')
plt.xlabel('시간(분)')
plt.show()

