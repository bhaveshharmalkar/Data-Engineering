1. Spark cluster
2. Spark Architecture
3. What is Databricks
4. Blob storage vs Data Lake
5. Magic Command
6. DBFS
7. App Registration (Service Principle) -> Create secret key (Just like password) - Bcz databricks need their credential to login into azure
8. Access Control -> Add role assignment -> Storage Blob Contributor (It grant which app want to access) 
9. Databricks utilities
    - dbutils.fs() -> For list down content 
    - dbutils.widgets -> For creating parameter
    - dbutils.secrets

10. Key vault -> Access control -> Add role assignment -> Key vault administrator -> Add our mail
    Key vault -> Secrets -> Generate -> Add secret key

11. Create scope in databricks /#secrets/createScope
12. Pyspark transformations
13. Delta lake
    - Write in delta format
    - Managed Delta Tables
    - External Delta Tables
14. Delta lake functionalities
    - Insert
    - Delete
        - Tombstoning (Delete records in transactional log logical way not in physical way. File remain as it is in the storage)
    - Data Versoning
    - Time Travel
    - Vacuum
    - Optimize
    - ZORDER BY()
    - Data Skipping
    - Autloader
    - Jobs & Pipelines


