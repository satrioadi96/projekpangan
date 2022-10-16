#from os.path import expanduser as ospath
#import numpy as np
import streamlit as st
import pandas as pd
from PIL import Image
import altair as alt

#st.set_page_config(layout="wide")
jen_pan = ('Beras', 'Daging Ayam', 'Daging Sapi', 'Telur Ayam',
         'Bawang Merah', 'Bawang Putih', 'Cabai Merah', 'Cabai Rawit',
         'Minyak Goreng', 'Gula Pasir')

def img_header():
    image = Image.open('img-title.jpg')
    st.image(image)
    '''Penyusun oleh **Satrio Adi Prawiro**'''
    '''[Email](mailto:prawiro.96@gmail.com) | [Github](https://github.com/satrioadi96) | [Linkedin](https://www.linkedin.com/in/satrio-adi-prawiro-64617a162)'''
    st.write('_________________')

def graph0(link):
    link = link.replace('\t', ' ')
    spot = pd.read_excel(link)
    spot_ = spot.replace('-',0)
    spot2 = spot_.drop(['No.', '11/2022'], axis=1)
    spot3 = spot2.melt('Provinsi', var_name='Periode(Bln)', value_name='Harga(Rp)')
    spot31 = spot3['Harga(Rp)'].astype(int)
    return spot31

    

    
    


st.sidebar.markdown("# Menelusuri Kondisi Pangan di Indonesia")

option = st.sidebar.selectbox('Daftar Bab/Section:',
                              ('Pendahuluan dan Data', 'Kesimpulan dan Daftar Pustaka'))

st.sidebar.markdown('''
                    Target:
    - deskripsi harga pangan setiap periode bulanan
    - daerah mana yang paling banyak produksi bahan pangan utama
    - menelaah pengaruh produksi terhadap harga maupun ekspor-impornya
    - model yang optimal untuk memperkuat pengaruhnya. 
                    ''')

if option == 'Pendahuluan dan Data' or option == '':
    img_header()
    '''
    > *Masyarakat di dunia, khususnya di Indonesia sejak lama memenuhi kebutuhan mereka dalam hal bahan pakaian (sandang), tempat tinggal/rumah (papan) dan makanan (pangan). Pangan merupakan kebutuhan bertahan hidup dengan mengonsumsi bahan yang layak dimakan dari alam. Sepanjang perjalanan sejarahnya, kebutuhan masyarakat ini pernah mengalami kejayaan dan kemakmuran hingga terpenuhi baik dalam dan luar negeri. Disisi lain, kekurangan pangan sering terjadi akibat bencana, baik dari alam (banjir, gempa, longsor) maupun manusia (perang dan konflik), sehingga tak pelak menimbulkan korban yang berjatuhan karena kelaparan, kekurangan gizi, dan penyakit lainnya hingga kematian.*
    '''
    st.image(Image.open('lag_banget.png'))
    
    '''
    Ringkasan data yang dikelompokkan dalam 10 jenis pangan berikut.
    '''
    st.image(Image.open('sepuluh pangan.png'))
    '''Dengan sumber data sekunder, ini akan dibagi dalam periode bulanan. Dengan jabaran: Harga, Produksi, dan Ekspor-Impor'''
    
    dfm = pd.read_excel("daerah/harga-pasar-modern-daerah.xls")
    dft = pd.read_excel("daerah/harga-pasar-tradisional-daerah.xls")
    
    dcm = dfm.copy()
    dct = dft.copy()
    
    indek = dcm.drop(['No.', '11/2022'], axis=1)
    indek2 = dct.drop(['No.', '11/2022'], axis=1)
    
    melet = indek.melt('Komoditas(Rp)', var_name='Periode(Bln)', value_name='Harga(Rp)')
    telem = indek2.melt('Komoditas(Rp)', var_name='Periode(Bln)', value_name='Harga(Rp)')
    
    '''____________________
#### Grafik Harga Jenis Pangan Tingkat Nasional (Pasar Modern)'''
    
    cmdty1 = st.selectbox(
        'Jenis Pangan',
        jen_pan)
    
    melet2 = melet[melet['Komoditas(Rp)']== cmdty1]
    melet2['Periode(Bln)']= pd.to_datetime(melet2['Periode(Bln)'])
    
    chart = alt.Chart(melet2).mark_line(
        point=alt.OverlayMarkDef(color="blue")
        ).encode(
    x=alt.X('Periode(Bln)'),
    y=alt.Y('Harga(Rp)'),
    color=alt.Color("Komoditas(Rp)")
    )

    
    st.altair_chart(chart, use_container_width=True)
    
    #
    momax = melet2[melet2['Komoditas(Rp)'] == cmdty1]['Harga(Rp)'].max()
    momin = melet2[melet2['Komoditas(Rp)'] == cmdty1]['Harga(Rp)'].min()
    moavg = melet2[melet2['Komoditas(Rp)'] == cmdty1]['Harga(Rp)'].mean()
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Harga Tertinggi", 'Rp'+str(momax)+',00')
    col2.metric("Harga Terendah", 'Rp'+str(momin)+',00')
    col3.metric("Harga Rata-rata", 'Rp'+str(round(moavg,2)))
    
    '''#### Grafik Harga Jenis Pangan Tingkat Nasional (Pasar Tradisional)'''
    
    cmdty2 = st.selectbox(
        'Jenis Pangan ',
        jen_pan)
    
    telem2 = telem[telem['Komoditas(Rp)']== cmdty2]
    #telem2['Periode(Bln)']= pd.to_datetime(telem2['Periode(Bln)'])
    
    chart = alt.Chart(telem2).mark_line(
        point=alt.OverlayMarkDef(color="blue")
        ).encode(
    x=alt.X('Periode(Bln)'),
    y=alt.Y('Harga(Rp)'),
    color=alt.Color("Komoditas(Rp)")
    )
    
    st.altair_chart(chart, use_container_width=True)
    
    #
    tramax = telem2[telem2['Komoditas(Rp)'] == cmdty2]['Harga(Rp)'].max()
    tramin = telem2[telem2['Komoditas(Rp)'] == cmdty2]['Harga(Rp)'].min()
    traavg = telem2[telem2['Komoditas(Rp)'] == cmdty2]['Harga(Rp)'].mean()
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Harga Tertinggi", 'Rp'+str(momax)+',00')
    col2.metric("Harga Terendah", 'Rp'+str(momin)+',00')
    col3.metric("Harga Rata-rata", 'Rp'+str(round(moavg,2)))
    
    '''__________________________'''
    
    '''#### Grafik Harga Jenis Pangan Tingkat Provinsi (Pasar Modern)'''
    


    
    '''#### Grafik Harga Jenis Pangan Tingkat Provinsi (Pasar Tradisional)'''
    
    '''#### Grafik Produksi Jenis Pangan Nasional'''
    
    
    '''
    
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


