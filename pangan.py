import streamlit as st
import pandas as pd
from PIL import Image
import altair as alt

#st.set_page_config(layout="wide")
jen_pan = ('Beras', 'Daging Ayam', 'Daging Sapi', 'Telur Ayam',
         'Bawang Merah', 'Bawang Putih', 'Cabai Merah', 'Cabai Rawit',
         'Minyak Goreng', 'Gula Pasir')
tymrk = ("Modern", "Tradisional")
popro = ('SEMUA PROVINSI', 'ACEH', 'SUMATERA UTARA', 'SUMATERA BARAT',
       'RIAU', 'KEPULAUAN RIAU', 'JAMBI', 'BENGKULU', 'SUMATERA SELATAN',
       'KEPULAUAN BANGKA BELITUNG', 'LAMPUNG', 'BANTEN', 'JAWA BARAT',
       'DKI JAKARTA', 'JAWA TENGAH', 'DI YOGYAKARTA', 'JAWA TIMUR',
       'BALI', 'NUSA TENGGARA BARAT', 'NUSA TENGGARA TIMUR',
       'KALIMANTAN BARAT', 'KALIMANTAN SELATAN', 'KALIMANTAN TENGAH',
       'KALIMANTAN TIMUR', 'KALIMANTAN UTARA', 'GORONTALO',
       'SULAWESI SELATAN', 'SULAWESI TENGGARA', 'SULAWESI TENGAH',
       'SULAWESI UTARA', 'SULAWESI BARAT', 'MALUKU', 'MALUKU UTARA',
       'PAPUA', 'PAPUA BARAT')

def img_header():
    image = Image.open('img-title.jpg')
    st.image(image)
    '''Penyusun oleh **Satrio Adi Prawiro**'''
    '''[Email](mailto:prawiro.96@gmail.com) | [Github](https://github.com/satrioadi96) | [Linkedin](https://www.linkedin.com/in/satrio-adi-prawiro-64617a162)'''
    '''[![Lisensi CC-BY 3.0](https://i.creativecommons.org/l/by/3.0/88x31.png)](http://creativecommons.org/licenses/by/3.0/)'''
    #'''[![image alt text](image URL link)](anchor link)'''
    #st.write('_________________')

# ----------------------------------------

st.sidebar.markdown("# Menelusuri Kondisi Pangan di Indonesia")

option = st.sidebar.selectbox('Daftar Bab/Section:',
                              ('Pendahuluan dan Data', 'Kesimpulan dan Daftar Pustaka'))

st.sidebar.markdown('''
                    Target:
    - deskripsi harga pangan setiap periode bulanan
    - menelaah pengaruh produksi terhadap harga
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
    '''Dengan sumber data sekunder, ini akan dibagi dalam periode bulanan dan tahunan. Dengan jabaran: Harga, Produksi, dan Ekspor-Impor'''
    
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
    st.caption('Gunakan gulir pada mouse (*scroll*) atau cubit touchpad dengan dua jari di dalam diagram/grafik untuk memperbesar dan memperkecil.')
    
    cmdty1 = st.selectbox(
        'Jenis Pangan dari Pasar Modern',
        jen_pan)
    
    melet2 = melet[melet['Komoditas(Rp)']== cmdty1]
    melet2['Periode(Bln)']= pd.to_datetime(melet2['Periode(Bln)'])
    
    chart = alt.Chart(melet2).mark_line(
        point=alt.OverlayMarkDef(color="")
        ).encode(
    x=alt.X('Periode(Bln)'),
    y=alt.Y('Harga(Rp)'),
    color=alt.Color("Komoditas(Rp)"),
    tooltip=['Komoditas(Rp)', 'Periode(Bln)', 'Harga(Rp)']
    ).interactive()
    st.altair_chart(chart, use_container_width=True)
    
    
    momax = melet2[melet2['Komoditas(Rp)'] == cmdty1]['Harga(Rp)'].max()
    momin = melet2[melet2['Komoditas(Rp)'] == cmdty1]['Harga(Rp)'].min()
    moavg = melet2[melet2['Komoditas(Rp)'] == cmdty1]['Harga(Rp)'].mean()
    
    st.write("Pada Pasar Modern, harga tertinggi dari jenis pangan "+cmdty1+" adalah Rp"+str(momax)+",00 dan harga terendahnya adalah Rp"+str(momin)+',00.')
    st.write("Rata-rata seharga Rp"+str(round(moavg,2))+'.')
    
    '''Dapat dilihat bahwa jenis pangan''' #keterangan blm selesai
    
    '''#### Grafik Harga Jenis Pangan Tingkat Nasional (Pasar Tradisional)'''
    
    cmdty2 = st.selectbox(
        'Jenis Pangan dari Pasar Tradisional',
        jen_pan)
    
    telem2 = telem[telem['Komoditas(Rp)']== cmdty2]
    telem2['Periode(Bln)']= pd.to_datetime(telem2['Periode(Bln)'])
    
    chart = alt.Chart(telem2).mark_line(
        point=alt.OverlayMarkDef(color="")
        ).encode(
    x=alt.X('Periode(Bln)'),
    y=alt.Y('Harga(Rp)'),
    color=alt.Color("Komoditas(Rp)"),
    tooltip=['Komoditas(Rp)', 'Periode(Bln)', 'Harga(Rp)']
    ).interactive()
    
    st.altair_chart(chart, use_container_width=True)
    
    tramax = telem2[telem2['Komoditas(Rp)'] == cmdty2]['Harga(Rp)'].max()
    tramin = telem2[telem2['Komoditas(Rp)'] == cmdty2]['Harga(Rp)'].min()
    traavg = telem2[telem2['Komoditas(Rp)'] == cmdty2]['Harga(Rp)'].mean()

    st.write("Pada Pasar Tradisional, harga tertinggi dari jenis pangan "+cmdty2+" adalah Rp"+str(tramax)+",00 dan harga terendahnya adalah Rp"+str(tramin)+',00.')
    st.write("Rata-rata seharga Rp"+str(round(traavg,2))+'.')
    
    '''__________________________'''
    '''#### Grafik Produksi Jenis Pangan Nasional (Tahunan)'''
    
    bwpt = 'produksi/produksi-bawang-putih.tsv'
    bwmr = 'produksi/produksi-bawang-putih.tsv'
    bras = 'produksi/produksi-beras.tsv'
    cbmr = 'produksi/produksi-cabai-merah.tsv'
    cbrw = 'produksi/produksi-cabai-rawit.tsv'
    dgym = 'produksi/produksi-daging-ayam.tsv'
    dgsp = 'produksi/produksi-daging-sapi.tsv'
    glps = 'produksi/produksi-gula-pasir.tsv'
    tlym = 'produksi/produksi-telur-ayam.tsv'
    mygr = 'produksi/produksi-minyak-goreng.tsv'
    
    ts_ble = (bras, dgym, dgsp, tlym, bwmr, bwpt, cbmr, cbrw, mygr, glps)
    
    prod = st.selectbox(
        'Jenis Pangan untuk Produksi',
        jen_pan)
    
    for i in range(0,len(ts_ble)):
        if prod == jen_pan[i]:
            tbl = pd.read_csv(ts_ble[i], sep="\t")
            tbl.rename(columns = {'Nama':'Tahun'}, inplace = True)

            diagram = alt.Chart(tbl).mark_bar(size=20).encode(
                x=tbl.columns[1]+':O',
                y=tbl.columns[2],
                tooltip=[tbl.columns[2]]
                ).properties(width=650)
            
            st.altair_chart(diagram, use_container_width=True)
            
            st.write("Beberapa tahun terakhir ini, jenis pangan "+jen_pan[i]+" memproduksi paling tinggi "+str(tbl[tbl.columns[2]].max())+" dan paling rendah "+str(tbl[tbl.columns[2]].min())+'.')
            st.write('Dalam satuan '+tbl.columns[2]+', rata-rata produksinya adalah '+str(round(tbl[tbl.columns[2]].mean(),2))+'.')

    '''__________________________'''
    #'''## Analisa dan Model'''
    '''#### Grafik sebaran korelasi antara harga dengan produksi jenis pangan'''
    
    col1, col2 = st.columns(2)
    
    jnpg_0 = ('Beras', 'Daging Ayam', 'Daging Sapi', 'Telur Ayam',
         'Bawang Merah', 'Bawang Putih','Cabai Rawit','Minyak Goreng')
    corlst = pd.read_csv('korelasi/korelasi.csv')
    

    with col1:
        markt = st.radio(
            "Jenis Pasar",
            tymrk)

    with col2:
        komdity = st.selectbox(
        'Jenis Pangan yang dikorelasikan',
        jnpg_0)
        
    
    for h in range(0,len(tymrk)):
            for i in range(0,len(jnpg_0)):
                if markt == tymrk[h] and komdity == jnpg_0[i]:
                    halt = alt.Chart(corlst[(corlst['Pasar']==tymrk[h]) & (corlst['Komoditas']==jnpg_0[i])]).mark_circle(
                        size=70,color='magenta',
                        ).encode(
                        x='Harga',
                        y='Produksi',
                        tooltip=['Komoditas','Tahun','Pasar','Harga','Produksi']
                        ).interactive()
                    
                    st.altair_chart(halt) #, use_container_width=True)
    
    '''__________________________'''
    
    '''#### Grafik Harga Jenis Pangan per Provinsi (Bulanan)'''
    st.caption('Info grafik tambahan')
    
    colA, colB, colC = st.columns(3)

    with colA:
        mrkt = st.radio(
            "Jenis Pasar per Provinsi",
            tymrk)

    with colB:
        cmdty3 = st.selectbox(
        'Jenis Pangan per Provinsi',
        jen_pan)
        
    with colC:
        provc = st.selectbox('Provinsi (Daerah)',popro)
        
    bm='-komoditas-bawang-merah.xls'
    bp='-komoditas-bawang-putih.xls'
    br='-komoditas-beras.xls'
    cm='-komoditas-cabai-merah.xls'
    cr='-komoditas-cabai-rawit.xls'
    da='-komoditas-daging-ayam.xls'
    ds='-komoditas-daging-sapi.xls'
    gp='-komoditas-gula-pasir.xls'
    mg='-komoditas-minyak-goreng.xls'
    ta='-komoditas-telur-ayam.xls'
        
    li_pgn = (br,da,ds,ta,bm,bp,cm,cr,mg,gp)
        
    for h in range(len(tymrk)):
        for i in range(len(jen_pan)):
            for j in range(len(provc)):
                if mrkt == tymrk[h] and cmdty3 == jen_pan[i] and provc == popro[j]:
                        laslast = pd.read_excel('./'+tymrk[h].lower()+'/harga-pasar-'+tymrk[h].lower()+li_pgn[i])
                        llss = laslast.drop(['No.', '11/2022'], axis=1).melt('Provinsi', var_name='Periode(Bln)', value_name='Harga(Rp)')
                        llss['Periode(Bln)']= pd.to_datetime(llss['Periode(Bln)'])
                        llss3 = llss[llss['Provinsi'] == popro[j]]
                        
                        borak = alt.Chart(llss3).mark_line(point=alt.OverlayMarkDef(color="")
                                                   ).encode(
                                                       x=alt.X('Periode(Bln)'),
                                                       y=alt.Y('Harga(Rp)'),
                                                       color=alt.Color("Provinsi"),
                                                       tooltip=['Provinsi', 'Periode(Bln)', 'Harga(Rp)']
                                                       ).interactive()
                                                   
                        st.altair_chart(borak, use_container_width=True)
    
    lsmax = llss3['Harga(Rp)'].max()
    lsmin = llss3['Harga(Rp)'].min()
    lsavg = llss3['Harga(Rp)'].mean()
    
    st.write("Pada Pasar "+tymrk[h]+" di Provinsi "+popro[j]
             +", harga pangan "+cmdty3+" per kilogram yang tertinggi adalah Rp"+str(lsmax)
             +",00 dan harga terendahnya adalah Rp"+str(lsmin)+',00. '
             +"Rata-rata seharga Rp"+str(round(lsavg,2))+'.')
    
    

    
elif option == 'Kesimpulan dan Daftar Pustaka':
    '''
## Bagaimana Kesimpulannya? Apakah ada Rekomendasi yang memungkinkan?

- Masyarakat (Publik) semestinya memantau lebih dengan adanya kenaikan harga yang signifikan bahkan melonjak dan produksi pangan yang bisa merosot setiap saat.
- Menjaga daya beli dengan membeli pangan seperlunya di pasar yang masih mengindikasikan harga yang murah dan wajar
- Publik bisa menjadikan infografis ini sebagai masukan untuk Pemerintah (khususnya instansi yang terkait) untuk tidak mengimpor bahan pangan secara tiba-tiba yang justru merosotkan penghasilan para petani dan pekebun. akan lebih baik stok dari petani dan pekebun sendiri sepenuhnya.
- Masukan berikutnya adalah ketika data-data yang ada masih terbatas, baik karena data yang hilang, periode bulanannya sedikit, maupun tidak tersedia. Ini bisa menjadi bias saat dianalisa dan implementasinya rancu (termasuk di bagian *scatterplot*), sehingga publik membutuhkan hasil implementasi data yang lebih akurat.
- Untuk grafis/diagram data-data saat ini menunjukkan:
    a. banyak jenis pangan seperti bawang dan cabai yang tidak stabil dalam 2 tahun terakhir ini, namun stok produksi naik signifikan
    b. untuk korelasi, ada yag bernilai negatif dan landai (harga pangan bisa turun sewaktu-waktu karena produksi pangan yang meningkat signifikan)
'''

    '''
## Daftar Pustaka

- Syakirotin, Muthiah.2022.*Ketahanan Pangan Sebelum dan Selama Pandemi Covid-19 di Kabupaten Bandung*.Jurnal.Bandung: Jurnal Ilmu Pertanian Indonesia
- Sadiyah, Halimatus.2022.*Taiwan Sebut Asal-usul Virus COVID-19 Bukan dari Pasar Wuhan*.https://www.cnbcindonesia.com/lifestyle/20220930102306-33-376204/taiwan-sebut-asal-usul-virus-covid-19-bukan-dari-pasar-wuhan (Diakses 9 Oktober 2022)
- P.S., Tommy & sef.2022.*Ini Awal Mula Perang Rusia-Ukraina, Akankah Segera Berakhir?*.https://www.cnbcindonesia.com/news/20220228064546-4-318875/ini-awal-mula-perang-rusia-ukraina-akankah-segera-berakhir/1. (Diakses 10 Oktober 2022)
- Nugroho, Agus D..2022.*Perang, Krisis Pangan, dan Diplomasi Jokowi*.https://news.detik.com/kolom/d-6168790/perang-krisis-pangan-dan-diplomasi-jokowi. (Diakses 10 Oktober 2022)
- Pusat Informasi Harga Pangan Strategis Nasional(PIHPS Nasional).2022.*Informasi Harga Pangan Antar Daerah*.https://hargapangan.id/. (Diakses 9-11 Oktober 2022)
- databooks,katadata.co.id.2022.*Portal data terlengkap dan terpercaya*.https://databoks.katadata.co.id/ (Diakses 18-19 Oktober 2022)
- Gartina, Dhani dan L. S., Lucky.2020.*STATISTIK PERKEBUNAN UNGGULAN NASIONAL 2019-2021*.Jakarta:Direktorat Jenderal Perkebunan Kementerian Pertanian Republik Indonesia
'''


