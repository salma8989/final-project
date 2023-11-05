Final Project Data Engineering 

#Set Up
1. Clone This Repo.
2. Run `make docker-build` for x86 user, or `make docker-build-arm` for arm chip user.


For Windows, open entrypoint.sh at VSCode, then change CRLF into LF and save. run 'make docker-build', so we can run make airflow.

---
```
## docker-build      - Build Docker Images (amd64) including its inter-container network.
## docker-build-arm  - Build Docker Images (arm64) including its inter-container network.
## postgres     - Run a Postgres container
## spark        - Run a Spark cluster, rebuild the postgres container, then create the destination tables
## jupyter			- Spinup jupyter notebook for testing and validation purposes.
## airflow			- Spinup airflow scheduler and webserver. 
## metabase			- Run a metabase container.
## clean			- Cleanup all running containers related to the challenge.
```

---

#Dataset
The Himalayan Database is a compilation of records for all expeditions that have climbed in the Nepal Himalaya. The database is based on the expedition archives of Elizabeth Hawley, a longtime journalist based in Kathmandu, and it is supplemented by information gathered from books, alpine journals and correspondence with Himalayan climbers.

1. The Members table describes each of the members on the climbing team and hired personnel who were significantly involved in the expedition.
2. The Expeditions table describes each of the climbing expeditions.
3. The Peaks table describes the mountaineering peaks of Nepal, one record for each peak.

![finpro-data-architecture](https://github.com/salma8989/final_project/assets/113493800/bdf6883d-0349-40fc-910f-92df7b607972)



Special thanks to Kang Thosan and Mentors.
Most of this configurations are from Kang Thosan lecture
