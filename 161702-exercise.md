# Exercises
---
## Exercise 5 "K-Means (2): Data Cleansing dan Online Advertisement"
### Time: 2017-04-07 until 2017-04-14
### Task
**[INDIVIDU]**
1. Register ke Databricks Community Edition.
2. Mencoba tutorial pada referensi [1] dengan cara membuat notebook di Databricks masing-masing.
3. Share link notebook dengan cara menuliskannya di file readme pada repositori Github kelompok.
Dataset untuk contoh web log dapat menggunakan data dari:
    * http://ita.ee.lbl.gov/html/contrib/NASA-HTTP.html
    * https://archive.ics.uci.edu/ml/index.html (cari tentang web log atau access log)
        * Anonymous Microsoft Web Data
        * MSNBC.com Anonymous Web Data
        * Syskill and Webert Web Page Ratings
    * http://ita.ee.lbl.gov/html/traces.html
    * https://www.quora.com/Are-there-any-free-large-datasets-in-the-format-of-an-Apache-access-log

**[KELOMPOK]**
1. Lanjutkan pemrosesan data UFO dengan melakukan data cleansing seperti pada tutorial [2] *chapter* 7.
2. Buat visualisasi tampilan K-means menggunakan pustaka `matplotlib` atau fungsi `display()` pada Databricks.
3. Kumpulkan notebook hasil pekerjaan di repositori Github masing-masing. Apabila kalian menggunakan notebook di Databricks, *copy*-kan public link notebook kalian di file readme.

### References
[1]“An Illustrated Guide to Advertising Analytics,” Databricks, 02-Feb-2016. [Daring]. Tersedia pada: https://databricks.com/blog/2016/02/02/an-illustrated-guide-to-advertising-analytics.html. [Diakses: 07-Apr-2017].  
[2] “jvns/pandas-cookbook,” GitHub. [Daring]. Tersedia pada: https://github.com/jvns/pandas-cookbook. [Diakses: 06-Apr-2017].  
[3] “Big Data Processing with Apache Spark - Part 5: Spark ML Data Pipelines,” InfoQ.   [Daring]. Tersedia pada: https://www.infoq.com/articles/apache-sparkml-data-pipelines. [Diakses: 06-Apr-2017].  


---
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

---
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

---
## Exercise 2
### Time: 2017-03-10 until 2017-03-17
### Task
1. Copy file tutorial [dari Google Drive](https://drive.google.com/open?id=0BwYyoQqEZfB_dU5aQWlWZUljYUU) folder **PySpark RDD Introduction**.
2. Kerjakan tutorial yang diberikan di video.
3. Buat sebuah repo di GitHub dan upload script notebook kalian di sana. Tuliskan nama dan NRP anggota kelompok di dalam file README.md.
4. Isikan URL repo GitHub kalian [di sini](https://docs.google.com/spreadsheets/d/1fMqlLKCxggr2B88oSVJWl4QOLium2t6QzE0vQ-RURww/edit?usp=sharing)

### References
1. [PySpark Jupyter Notebook Template](https://github.com/munif/big-data-course/blob/master/notebook/PySpark%20Jupyter%20Notebook%20Template.ipynb)

---
## Exercise 1
### Time: 2017-02-17 until 2017-02-24
### References
1. [Hortonworks Hadoop Sandbox](http://hortonworks.com/products/sandbox/)  
2. [Hadoop Tutorial – Getting Started with HDP](http://hortonworks.com/hadoop-tutorial/hello-world-an-introduction-to-hadoop-hcatalog-hive-and-pig/)  
3. [All tutorials](http://hortonworks.com/tutorials/)  

### Tasks
Do the tutorial at reference [2]. Save your works and present your Zeppelin Notebook.
