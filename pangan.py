#from os.path import expanduser as ospath
#import numpy as np
import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

def img_header():
    image = Image.open('img-title.jpg')
    st.image(image)
    st.markdown("Penyusun oleh **Satrio Adi Prawiro**")
    st.markdown("[Email](mailto:prawiro.96@gmail.com) | [Github](https://github.com/satrioadi96) | [Linkedin](https://www.linkedin.com/in/satrio-adi-prawiro-64617a162)")
    st.write('_________________')
    
def graphic_line_cmdty(link, psr, cmdty):
    #link = '.\daerah\harga-pasar-'+psr+'-daerah.xls'
    df_hpmkb = pd.read_excel(link)
    
    prov = df_hpmkb[df_hpmkb['Komoditas(Rp)'] == cmdty]['Harga']
    period = df_hpmkb[df_hpmkb['Komoditas(Rp)'] == cmdty]['Periode']
    
    plt.figure(figsize=(40, 10))
    plt.plot(period,prov, color='grey', linewidth = 3, marker='o', markerfacecolor='grey', markersize=9)
    plt.grid(color='darkgray', linestyle=':', linewidth=0.5)
    plt.xlabel('Periode (Bulan)')
    plt.ylabel('Harga (Rp)')
    plt.savefig('.\output1\output-'+psr+'-'+cmdty+'.jpg', dpi=300)
    
#________________________________

st.sidebar.markdown("# Menelusuri Kondisi Pangan di Indonesia")

option = st.sidebar.selectbox(
    'Daftar Bab/Section:',
    ('Pendahuluan','Data dan Visualisasi', 'Analisa dan Model', 'Rekomendasi dan Kesimpulan','Daftar Pustaka')
)

if option == 'Pendahuluan' or option == '':
    img_header()
    '''
    ## PENDAHULUAN
### Latar belakang
    
> *Masyarakat di dunia, khususnya di Indonesia sejak lama memenuhi kebutuhan mereka dalam hal bahan pakaian (sandang), tempat tinggal/rumah (papan) dan makanan (pangan). Pangan merupakan kebutuhan bertahan hidup dengan mengonsumsi bahan yang layak dimakan dari alam. Sepanjang perjalanan sejarahnya, kebutuhan masyarakat ini pernah mengalami kejayaan dan kemakmuran hingga terpenuhi baik dalam dan luar negeri. Disisi lain, kekurangan pangan sering terjadi akibat bencana, baik dari alam (banjir, gempa, longsor) maupun manusia (perang dan konflik), sehingga tak pelak menimbulkan korban yang berjatuhan karena kelaparan, kekurangan gizi, dan penyakit lainnya hingga kematian.*

Beberapa tahun terakhir ini, [ pandemi yang bernama COVID-19 disebabkan oleh Virus SARS-CoV-2](https://www.cnbcindonesia.com/lifestyle/20220930102306-33-376204/taiwan-sebut-asal-usul-virus-covid-19-bukan-dari-pasar-wuhan)  yang muncul akhir tahun 2019 dari Wuhan, China dan menghancurkan bahan-bahan pangan didunia, termasuk distribusinya. Muthiah (2022) menjelaskan dari sumber _World Food Programme_ yang menyebutkan pada tahun 2020 terdapat 768 juta jiwa yang mengalami kelaparan kronis akibat meningkatnya kemiskinan dunia dalam masa pandemi COVID-19. Dalam menghadapi penyebaran COVID-19, sektor pertanian menjadi kebutuhan prioritas karena berhubungan langsung dengan ketahanan pangan nasional. Jawa Barat sebagai lumbung pangan nasional terdampak karena meningkatnya jumlah penduduk miskin. Misal pada tahun 2021, Kabupaten Bandung mengalami kemiskinan ekstrem, yaitu 2,64%. Hal ini akan memengaruhi ketahanan pangan khususnya, dalam aspek keterjangkauan.

Belum lagi ditambah dengan [peristiwa perang dan koflik yang besar, antara Ukraina dan Rusia](https://www.cnbcindonesia.com/news/20220228064546-4-318875/ini-awal-mula-perang-rusia-ukraina-akankah-segera-berakhir/1) sebagai dua negara produsen dan pengekspor gandum terbesar di dunia yang dimulai sejak 24 Februari 2022. Tak bisa dipungkiri, banyak negara terutama di Afrika, Eropa Timur, dan Asia Tengah yang [bergantung pada impor bahan pangan](https://news.detik.com/kolom/d-6168790/perang-krisis-pangan-dan-diplomasi-jokowi) dari kedua negara. Kemudian, dalam konteks makanan, rantai pasok terkait dengan dua kategori rantai pasok, yakni rantai pasok komoditas pokok seperti beras, gandum, jagung, kedelai dan rantai pasok komoditas bernilai tinggi seperti buah dan sayur-sayuran. Nah, komoditas bahan pokok yang bergantung pada impor inilah yang akan langsung terkena imbas dari kebijakan pembatasan ekpor komoditas pangan dari sebelas negara yang disebutkan Jokowi. Pangan berbahan baku gandum, kedelai, minyak kedelai, terigu, daging, dan lainnya akan mengalami kelangkaan suplai, lalu mengerek harga secara drastis, yang akan merongrong daya beli masyarakat.

Oleh karena itu, Penyusun melakukan penelusuran mengenai kondisi bahan pangan utama dalam negeri, mengenai harga pangan, daerah mana yang paling banyak produksi bahan pangan utama, menelaah pengaruhnya terhadap harga maupun ekspor-impornya, serta model yang optimal untuk memperkuat pengaruhnya. Dengan ini diharapkan bisa menemukan solusi yang tepat untuk direkomendasikan secara publik dan khususnya untuk instansi pemerintah yang terkait. 
'''
    
elif option == 'Data dan Visualisasi':
    img_header()
    
    '''
    ## Data dan Visualisasi

### Deskripsi Data
Data yang akan digunakan adalah data dengan 10 jenis pangan pokok di Indonesia, antara lain:

- beras
- daging ayam 
- daging sapi
- telur ayam
- bawang merah 
- bawang putih
- cabai merah 
- cabai rawit
- minyak goreng
- gula pasir

data ini terbagi dalam periode waktu bulanan yang akan ditampilkan dalam aplikasi web streamlit dengan Grafik Data. 

### Grafik Data
Data akan ditampilkan beserta deskripsinya dalam grafik berikut.
> a.  grafik/diagram garis (*line*) mengenai:
> - pergerakan harga setiap komoditas pangan (periode bulanan)
> - pergerakan harga setiap provinsi (pokok setiap provinsi)

> b. grafik *scatterplot/bubble* untuk korelasi :
> - produksi dalam negeri dengan harga

> c. grafik model mesin pembelajaran (*Machine learning*) untuk (data aktual dan prediksi):
> - produksi dalam negeri dengan harga

### Sumber dan Metode Data
Sumbernya meliputi berbagai website dari [BPS](https://www.bps.go.id/), [PIHPS](https://hargapangan.id), Kementan dll.

Karena data ini diperoleh dari sumber yang telah ada (internet) dan bukan survei, maka metode yang digunakan adalah metode sekunder untuk pengumpulan data.


### Visualisasi Data

Berikut grafik untuk pergerakan harga setiap komoditas pangan (periode bulanan) di seluruh Indonesia
    '''
    "#### Grafik Harga Bahan Pangan Nasional dari tahun 2020-2022"
    
    komoditas = ('Beras', 'Daging Ayam', 'Daging Sapi', 'Telur Ayam',
       'Bawang Merah', 'Bawang Putih', 'Cabai Merah', 'Cabai Rawit',
       'Minyak Goreng', 'Gula Pasir')
    
    col1, col2 = st.columns(2)

    with col1:
        market = st.selectbox(
        "Jenis Pasar",
        ("Tradisional", "Modern")
    )

    with col2:
        comodity = st.selectbox(
        "Komoditas Pangan",
        komoditas
    )
    
    if market == 'Tradisional':
        table1 = '.\daerah\harga-pasar-tradisional-daerah.xls'
        for pang in komoditas:
            if pang :
                graphic_line_cmdty(table1, 'tradisional', pang)
    elif market == 'Modern':
        table2 = '.\daerah\harga-pasar-tradisional-modern.xls'
        for ngan in komoditas:
            if ngan :
                graphic_line_cmdty(table2, 'modern', ngan)

    
elif option == 'Analisa dan Model':
    img_header()
    st.write("""## Analisa dan Model""")
    '''
    Untuk Analisa ini Akan disusun dengan Model Yang Optimal dan akan diupdate nanti.
    '''

elif option == 'Rekomendasi dan Kesimpulan':
    '''
    ## Bagaimana Kesimpulannya? Apakah ada Rekomendasi yang memungkinkan?
    
    Dengan melihat Grafik Harga setiap komoditas pangan yang lebih dari signifikan, jelas Pemerintah (Khusus untuk Kementerian Pertanian, Kementerian Perdagangan, dan yang terkait lainnya) mesti lebih memerhatikan kebutuhan rakyatnya supaya tidak merosot daya belinya.
    Bahkan bagi Wilayah Indonesia Bagian Timur yang banyak komoditas pangan yang melonjak harganya. Ini juga diperparah dengan data dari daerah-daerah lain yang tidak dipantau yang memperparah kondisi pangan yang sebenarnya.
    
    Semestinya diperlukan tinjauan dan mendaur ulang program2 lama yang bisa efektif meningkatkan produksi pangan dalam negeri, dan setidaknya bisa mengimbangi ekspor-impor agar semakin kuat ketersediaan bahan-bahan tersebut dalan kondisi terbaik.
    
    '''
elif option == 'Daftar Pustaka':
    '''
    ## Daftar Pustaka

    - Syakirotin, Muthiah.2022.*Ketahanan Pangan Sebelum dan Selama Pandemi Covid-19 di Kabupaten Bandung*.Jurnal.Bandung: Jurnal Ilmu Pertanian Indonesia
    - Sadiyah, Halimatus.2022.*Taiwan Sebut Asal-usul Virus COVID-19 Bukan dari Pasar Wuhan*.https://www.cnbcindonesia.com/lifestyle/20220930102306-33-376204/taiwan-sebut-asal-usul-virus-covid-19-bukan-dari-pasar-wuhan (Diakses 9 Oktober 2022)
    - P.S., Tommy & sef.2022.*Ini Awal Mula Perang Rusia-Ukraina, Akankah Segera Berakhir?*.https://www.cnbcindonesia.com/news/20220228064546-4-318875/ini-awal-mula-perang-rusia-ukraina-akankah-segera-berakhir/1. (Diakses 10 Oktober 2022)
    - Nugroho, Agus D..2022.*Perang, Krisis Pangan, dan Diplomasi Jokowi*.https://news.detik.com/kolom/d-6168790/perang-krisis-pangan-dan-diplomasi-jokowi. (Diakses 10 Oktober 2022)
    - Pusat Informasi Harga Pangan Strategis Nasional(PIHPS Nasional).2022.Informasi Harga Pangan Antar Daerah.https://hargapangan.id/. (Diakses 9-11 Oktober 2022)
    '''



