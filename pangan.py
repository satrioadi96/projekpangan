#from os.path import expanduser as ospath
import numpy as np
import streamlit as st
import pandas as pd
from PIL import Image
#import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

def img_header():
    image = Image.open('img-title.jpg')
    st.image(image)
    st.markdown("Penyusun oleh **Satrio Adi Prawiro**")
    st.markdown("[Email](mailto:prawiro.96@gmail.com) | [Github](https://github.com/satrioadi96) | [Linkedin](https://www.linkedin.com/in/satrio-adi-prawiro-64617a162)")
    st.write('_________________')


st.sidebar.markdown("# Menelusuri Kondisi Pangan di Indonesia")

option = st.sidebar.selectbox('Daftar Bab/Section:',
                              ('Pendahuluan dan Data', 'Kesimpulan dan Daftar Pustaka'))

if option == 'Pendahuluan dan Data' or option == '':
    img_header()
    '''
    ## PENDAHULUAN
    ### Latar belakang
    Beberapa tahun terakhir ini, 
    [ pandemi yang bernama COVID-19 disebabkan oleh Virus SARS-CoV-2](https://www.cnbcindonesia.com/lifestyle/20220930102306-33-376204/taiwan-sebut-asal-usul-virus-covid-19-bukan-dari-pasar-wuhan)  yang muncul akhir tahun 2019 dari Wuhan, China dan menghancurkan bahan-bahan pangan didunia, termasuk distribusinya.
    Semain parah dengan [peristiwa perang dan koflik yang besar, antara Ukraina dan Rusia](https://www.cnbcindonesia.com/news/20220228064546-4-318875/ini-awal-mula-perang-rusia-ukraina-akankah-segera-berakhir/1) sebagai dua negara produsen dan pengekspor gandum terbesar di dunia yang dimulai sejak 24 Februari 2022. Akibatnya seluruh dunia, khususnya Indonesia [bergantung pada impor bahan pangan](https://news.detik.com/kolom/d-6168790/perang-krisis-pangan-dan-diplomasi-jokowi) sehingga mengerek harga secara drastis, yang akan merongrong daya beli masyarakat.

    Oleh karena itu, Penyusun melakukan penelusuran mengenai kondisi bahan pangan utama dalam negeri, mengenai harga pangan, daerah mana yang paling banyak produksi bahan pangan utama, menelaah pengaruhnya terhadap harga maupun ekspor-impornya, serta model yang optimal untuk memperkuat pengaruhnya. 
    Dengan ini diharapkan bisa menemukan solusi yang tepat untuk direkomendasikan secara publik dan khususnya untuk instansi pemerintah yang terkait. 
    '''
    
    '''
    ## Data dan Visualisasi
    ### Sumber dan Metode Data
    Sumbernya meliputi berbagai website dari [BPS](https://www.bps.go.id/), [PIHPS](https://hargapangan.id), Kementan dll.
    Karena data ini diperoleh dari sumber yang telah ada (internet) dan bukan survei, maka metode yang digunakan adalah metode sekunder untuk pengumpulan data.


    ### Visualisasi Data
    Berikut grafik untuk pergerakan harga setiap komoditas pangan (periode bulanan) di seluruh Indonesia

    #### Grafik Harga Bahan Pangan Nasional dari tahun 2020-2022
    
    ## Analisa dan Model
    Untuk Analisa ini Akan disusun dengan Model Yang Optimal dan akan diupdate nanti.
    '''
    
elif option == 'Kesimpulan dan Daftar Pustaka':
    '''
## Bagaimana Kesimpulannya? Apakah ada Rekomendasi yang memungkinkan?

Dengan melihat Grafik Harga setiap komoditas pangan yang lebih dari signifikan, jelas Pemerintah (Khusus untuk Kementerian Pertanian, Kementerian Perdagangan, dan yang terkait lainnya) mesti lebih memerhatikan kebutuhan rakyatnya supaya tidak merosot daya belinya.
Bahkan bagi Wilayah Indonesia Bagian Timur yang banyak komoditas pangan yang melonjak harganya. Ini juga diperparah dengan data dari daerah-daerah lain yang tidak dipantau yang memperparah kondisi pangan yang sebenarnya.

Semestinya diperlukan tinjauan dan mendaur ulang program2 lama yang bisa efektif meningkatkan produksi pangan dalam negeri, dan setidaknya bisa mengimbangi ekspor-impor agar semakin kuat ketersediaan bahan-bahan tersebut dalan kondisi terbaik.

'''

    '''
## Daftar Pustaka

- Syakirotin, Muthiah.2022.*Ketahanan Pangan Sebelum dan Selama Pandemi Covid-19 di Kabupaten Bandung*.Jurnal.Bandung: Jurnal Ilmu Pertanian Indonesia
- Sadiyah, Halimatus.2022.*Taiwan Sebut Asal-usul Virus COVID-19 Bukan dari Pasar Wuhan*.https://www.cnbcindonesia.com/lifestyle/20220930102306-33-376204/taiwan-sebut-asal-usul-virus-covid-19-bukan-dari-pasar-wuhan (Diakses 9 Oktober 2022)
- P.S., Tommy & sef.2022.*Ini Awal Mula Perang Rusia-Ukraina, Akankah Segera Berakhir?*.https://www.cnbcindonesia.com/news/20220228064546-4-318875/ini-awal-mula-perang-rusia-ukraina-akankah-segera-berakhir/1. (Diakses 10 Oktober 2022)
- Nugroho, Agus D..2022.*Perang, Krisis Pangan, dan Diplomasi Jokowi*.https://news.detik.com/kolom/d-6168790/perang-krisis-pangan-dan-diplomasi-jokowi. (Diakses 10 Oktober 2022)
- Pusat Informasi Harga Pangan Strategis Nasional(PIHPS Nasional).2022.Informasi Harga Pangan Antar Daerah.https://hargapangan.id/. (Diakses 9-11 Oktober 2022)
'''


