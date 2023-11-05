Halo Kang Thosan, terima kasih sudah mengajar selama di bootcamp. Banyak ilmu baru dan banyak perlu belajar.
Ini hasil final projectnya, namun masih ada kendala :
1. Saat run make jupyter, ada error :
PS C:\Users\asusa\Downloads\final-project> make jupyter
'__________________________________________________________'
'Creating Jupyter Notebook Cluster at http://localhost:9999 ...'
'__________________________________________________________'
time="2023-11-05T07:44:41+07:00" level=warning msg="Found orphan containers ([dataeng-spark-worker-1 dataeng-spark-master dataeng-postgres]) for this project. If you removed or renamed this service in your compose file, you can run this command with the --remove-orphans flag to clean it up."
[+] Running 1/1
 ✔ Container dibimbing-jupyter  Started                                                                 5.9s 
'Created...'
'Processing token...'
cut: the delimiter must be a single character
Try `cut --help' for more information.
make: *** [jupyter] Error 1

2. Saat buka http://localhost:8081/, belum bisa running dag.
Akhirnya running manual di python.
Error berada di folder logs.
[2023-11-05, 03:15:01 UTC] {taskinstance.py:1935} ERROR - Task failed with exception
Traceback (most recent call last):
  File "/home/airflow/.local/lib/python3.9/site-packages/airflow/providers/apache/spark/operators/spark_submit.py", line 156, in execute
    self._hook.submit(self._application)
  File "/home/airflow/.local/lib/python3.9/site-packages/airflow/providers/apache/spark/hooks/spark_submit.py", line 422, in submit
    raise AirflowException(
airflow.exceptions.AirflowException: Cannot execute: spark-submit --master spark://dataeng-spark-master:7077 --name arrow-spark /spark-scripts/transform.py. Error code is: 1.


3. Sudah menambah database di metabase, saat mau buat query SQL, tidak keluar hasilnya.
muncul ERROR: relation "public.expeditions_merge" does not exist Position: 162
query :
select count (distinct expedition_id)
from public.expeditions_merge;

Mohon koreksinya kang Thosan, terlampir documentation-screenshoot saat kendala.
Terima kasih 

