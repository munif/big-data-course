# Exercises

## Exercise 4 "K-means Clustering"
### Time: 2017-03-31 until 2017-04-07
### Task
1. Jalankan contoh tutorial tentang K-means clustering [1].
2. Lakukan proses clustering menggunakan data [UFO Sightings](https://www.kaggle.com/NUFORC/ufo-sightings). Data yang dapat di-*cluster*  adalah data koordinat *latitude* dan *longitude*.  
Tahapan *clustering*-nya adalah sebagai berikut:  
    1. Melakukan *data cleansing* untuk data koordinat yang kosong atau bernilai 0.   
    Data yang kosong dapat: (a) dihapus, (b) diganti dengan nilai avg, max, min, atau nilai *default* yang lain.
    2. Melakukan proses *clustering*.
    3. Menambahkan visualisasi data hasil *cluster* ke dalam diagram Cartesian menggunakan pustaka `matplotlib`.

### References
1. [Clustering - RDD Based Clustering](https://spark.apache.org/docs/latest/mllib-clustering.html#k-means)
## Exercise 3 "Frequent Pattern Mining"
### Time: 2017-03-17 until 2017-03-24
### Task
1. Jalankan contoh tutorial tentang Frequent Pattern Mining [1].
2. Review paper mengenai frequent pattern mining (FP-growth algorithm) [2]. Panjang review 3-4 paragraf yang berisi tentang: 
    * latar belakang permasalahan dan output yang diharapkan,
    * tahapan metode yang penting dan apa keunggulannya,
    * kesimpuan dan saran dari paper tersebut.
3. Buatlah sebuah dataset sendiri untuk diproses menggunakan frequent pattern mining. Contoh dataset yang mungkin bisa dibuat: daftar menu makanan sehari-hari, daftar situs yang sering diakses bersamaan dalam satu waktu, dan sebagainya.  
Setelah membuat dataset, proseslah dataset tersebut menggunakan frequent pattern mining.

### References
1. [Frequent Pattern Mining - RDD-based API](https://spark.apache.org/docs/latest/mllib-frequent-pattern-mining.html)
2. J. Han, J. Pei, and Y. Yin, "Mining Frequent Patterns Without Candidate Generation," in Proceedings of the 2000 ACM SIGMOD International Conference on Management of Data, New York, NY, USA, 2000, pp. 1–12.

## Exercise 2
### Time: 2017-03-10 until 2017-03-17
### Task
1. Copy file tutorial [dari Google Drive](https://drive.google.com/open?id=0BwYyoQqEZfB_dU5aQWlWZUljYUU) folder **PySpark RDD Introduction**.
2. Kerjakan tutorial yang diberikan di video.
3. Buat sebuah repo di GitHub dan upload script notebook kalian di sana. Tuliskan nama dan NRP anggota kelompok di dalam file README.md.
4. Isikan URL repo GitHub kalian [di sini](https://docs.google.com/spreadsheets/d/1fMqlLKCxggr2B88oSVJWl4QOLium2t6QzE0vQ-RURww/edit?usp=sharing)

### References
1. [PySpark Jupyter Notebook Template](https://github.com/munif/big-data-course/blob/master/notebook/PySpark%20Jupyter%20Notebook%20Template.ipynb)

## Exercise 1
### Time: 2017-02-17 until 2017-02-24
### References
1. [Hortonworks Hadoop Sandbox](http://hortonworks.com/products/sandbox/)  
2. [Hadoop Tutorial – Getting Started with HDP](http://hortonworks.com/hadoop-tutorial/hello-world-an-introduction-to-hadoop-hcatalog-hive-and-pig/)  
3. [All tutorials](http://hortonworks.com/tutorials/)  

### Tasks
Do the tutorial at reference [2]. Save your works and present your Zeppelin Notebook.
